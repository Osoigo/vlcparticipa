load Rails.root.join("app", "models", "verification", "residence.rb")

class Verification::Residence
  validate :document_number_length

  def save
    return false unless valid?

    user.take_votes_if_erased_document(document_number, document_type)

    update_user_with_census_data
  end

  private

    def document_number_length
      return if errors.any?

      unless document_number_length_valid?
        errors.add(:document_number, :wrong_length, count: 9)
        store_failed_attempt
        Lock.increase_tries(user)
      end
    end

    def document_number_length_valid?
      return false if (document_type != "2") && (!document_number.present? || (document_number.length != 9))

      true
    end

    def update_user_with_census_data
      habitante = census_data.datos_habitante
      vivienda = census_data.datos_vivienda

      user.update(document_number: document_number, # rubocop:disable Rails/SaveBang
                  document_type: document_type,
                  geozone: geozone,
                  date_of_birth: date_of_birth.in_time_zone.to_datetime,
                  gender: gender,
                  residence_verified_at: Time.current,
                  nIA: habitante[:nia],
                  name: habitante[:nombre],
                  first_name: habitante[:primer_apellido],
                  last_name: habitante[:segundo_apellido],
                  municipality_of_birth: habitante[:municipio_nacimiento],
                  province_of_birth: habitante[:provincia_nacimiento],
                  country_of_birth: habitante[:pais_nacimiento],
                  nationality: habitante[:nacionalidad],
                  dc: habitante[:letra],
                  census_last_modification_at: habitante[:fecha_ultima_modificacion],
                  census_created_at: habitante[:fecha_alta_inscripcion],
                  collective_entity: habitante[:entidad_colectiva],
                  singular_entity: habitante[:entidad_singular],
                  core: habitante[:nucleo],
                  single_entity_code: habitante[:codigo_unico_entidad],
                  census_phone: habitante[:telefono],
                  level_of_training: habitante[:nivel_instruccion],
                  permit_expiration_at: habitante[:fecha_caducidad_permiso],
                  protected_hab: habitante[:habitante_protegido],

                  district: vivienda[:distrito],
                  section: vivienda[:seccion],
                  sheet_number: vivienda[:numero_hoja],
                  province: vivienda[:provincia],
                  municipality: vivienda[:municipio],
                  acronym: vivienda[:acronimo],
                  type_road: vivienda[:tipovia],
                  street_name: vivienda[:nombreCalle],
                  access: vivienda[:numero],
                  km: vivienda[:kilometro],
                  stairs: vivienda[:escalera],
                  floor: vivienda[:planta],
                  door: vivienda[:puerta],
                  zip_code: vivienda[:codigo_postal],
                  full_address: vivienda[:direccion_planchada])
    end
end
