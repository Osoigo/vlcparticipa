#!/bin/bash
# Este script necesita que el client de minio tenga un alias que apunte al bucket de valencia
# Por ejemplo habiendo ejecutado este comando anteriormente: mc alias set valencia https://s3.gra.io.cloud.ovh.net/ user pass
#
# También necesita que el usuario que ejecuta el script tenga la clave pública de seguridad@osoigo.com
#   gpg --import seguridad.gpg.pub

export PATH=$PATH:/usr/local/bin

usage() {
  echo "Usage: $0 [-t <day|month|week>] backup_name" 1>&2
  exit 1
}

encrypt() {
  path=$1
  gpg --batch --yes --encrypt --recipient seguridad@osoigo.com --trust-model always $path
  rm -f $path
}

clean_old_local_backups() {
  path=$1
  keep=$2
  # Borrar backups viejos en local
  cd $path
  backups=($(ls -r))
  for item in ${backups[@]:${keep}}; do
    find $item -type f -exec shred -u {} \;
    rm -rf $item
  done
}

clean_old_remote_backups() {
  path=$1
  keep=$2
  # Borrar backups viejos en el almacenamiento S3
  backups=($(mcli ls --json ${path} | jq -r ".key" | sort -n -r))
  for item in ${backups[@]:${keep}}; do
    mcli rm -r -q --force ${path}/${item}
  done
}

get_database_field() {
  file=$1
  field=$2

  value=$(grep $field $file | cut -d: -f2)
  # remove leading whitespace characters
  value="${value#"${value%%[![:space:]]*}"}"
  # remove trailing whitespace characters
  value="${value%"${value##*[![:space:]]}"}"
  printf '%s' "$value"
}

set -e
while getopts "t:" o; do
  case "${o}" in
  t)
    BACKUP_TYPE=${OPTARG}
    [ "$BACKUP_TYPE" == "day" ] || [ "$BACKUP_TYPE" == "month" ] || [ "$BACKUP_TYPE" == "week" ] || usage
    ;;
  esac
done

shift $(($OPTIND - 1))

# La carpeta shared de consul
PROJECT_FOLDER=/var/consul/shared
# Nombre del proyecto
PROJECT_NAME=valencia-pre
# Nombre del bucket donde se guarda el backup
S3_BACKUP_BUCKET_NAME=valencia
# Nombre del backup, por defecto el día en formato YYYYMMDD
NAME=${1:-$(date "+%Y%m%d")}

if [ -z "${BACKUP_TYPE}" ]; then
  BACKUP_TYPE="day"
fi

# DEFAULT SETTINGS
SERVICES_HOME=$HOME

BACKUP_FOLDER=${SERVICES_HOME}/backups
LOCAL_KEEP=1
if [ "$BACKUP_TYPE" == "month" ]; then
  KEEP=12
elif [ "$BACKUP_TYPE" == "week" ]; then
  KEEP=4
  if [[ $(date '+%d') == '01' ]]; then
    # los primeros días de mes se hace backup mensual, no semanal
    exit 0
  fi
else
  KEEP=6
  if [[ $(date '+%d') == '01' ]]; then
    # los primeros días de mes se hace backup mensual, no diario
    exit 0
  fi
fi

echo Backup ${NAME} for project ${PROJECT_NAME}

s3_backup_base_path=backup/${S3_BACKUP_BUCKET_NAME}/${PROJECT_NAME}/${BACKUP_TYPE}
s3_backup_dir=${s3_backup_base_path}/${NAME}
backup_base_path=${BACKUP_FOLDER}/${PROJECT_NAME}/${NAME}

if [ ! -d $backup_base_path/config ]; then
  mkdir -p $backup_base_path/config
fi

cp $PROJECT_FOLDER/config/database.yml $backup_base_path/config/database.yml
encrypt $backup_base_path/config/database.yml
cp $PROJECT_FOLDER/config/secrets.yml $backup_base_path/config/secrets.yml
encrypt $backup_base_path/config/secrets.yml

echo ${DATABASE_NAME} database backup
host=$(get_database_field $PROJECT_FOLDER/config/database.yml host)
db_name=$(get_database_field $PROJECT_FOLDER/config/database.yml database)
username=$(get_database_field $PROJECT_FOLDER/config/database.yml username)
password=$(get_database_field $PROJECT_FOLDER/config/database.yml password)
database_url="postgresql://${username}:${password}@${host}:5432/${db_name}"
db_dump_filename="${backup_base_path}/database.dump"
pg_dump \
  --clean \
  --create \
  --format=custom \
  --compress=9 \
  --file=${db_dump_filename} \
  $database_url
encrypt $db_dump_filename

cd $PROJECT_FOLDER/storage
tar czf ${backup_base_path}/storage.tar .
cd -
encrypt $backup_base_path/storage.tar

mcli cp -r -q ${backup_base_path}/ ${s3_backup_dir}/

clean_old_local_backups ${BACKUP_FOLDER}/${PROJECT_NAME} $LOCAL_KEEP
clean_old_remote_backups $s3_backup_base_path $KEEP
