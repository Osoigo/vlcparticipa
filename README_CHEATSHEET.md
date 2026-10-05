# Guía básica para la personalización del contenido desde el `Administrador` de Consul

## Página de Inicio

### Encabezado

Se puede modificar el texto y enlace desde: **Contenido del sitio > Homepage > Encabezado**

Pero las imágenes al ser en dos idiomas lo deberán modificar los desarrolladores.

Recordar que está en dos idiomas, por lo que es necesario añadir la traducción también.

### Columnas

Las tres columnas de la página de inicio se pueden modificar desde **Contenido del sitio > Homepage > Tarjetas**

Pero las imágenes al ser en dos idiomas lo deberán modificar los desarrolladores.

Recordar que está en dos idiomas, por lo que es necesario añadir la traducción también.

## Cambios en texto como menú o avisos

En **Contenido del sitio > Personalizar textos** nos encontraremos con algunas variables de texto que podemos modificar.

Utiliza `Ctrl + F` para buscar en la página el texto a cambiar. Y navega entre las diferentes pestañas e idiomas.

Por ejemplo: Renombramos en el menú *Presupuestos participativos* por *Ediciones* en **Plantillas > `layouts.header.budgets`**. O *Ayuda* por *Más Información* en **Plantillas > `layouts.header.help`**.

Recordar siempre que está en dos **idiomas** y que es necesario **Guardar cambios**.

## Subida de ficheros para utilizarlos en otros apartados

Desde **Contenido del sitio > Documentos** podremos subir diferentes documentos y copiar sus direcciones para utilizarlos en otros apartados como en *Más información*.

Solo debemos clicar en el botón de **Subir un documento** y seguir los pasos.

Cuando lo queramos utilizar, solo debemos hacer *clic derecho* en **Descargar archivo** y seleccionar *Copiar dirección de enlace*. Ahora tendremos copiado el enlace al archivo en el portapapeles y podremos pegarlo para crear un link.

## Páginas personalizadas y apartado de *Más Información*

Desde **Contenido del sitio > Personalizar páginas** podremos crear y modificar las páginas informativas.

Por un lado tenemos los apartados legales que se muestran en el pie de página y por otro el contenido que aparece en forma de acordeón en el apartado de *Más Información*.

Además desde **Orden en la página «Más información** arrastrando cada línea podremos ordenar los temas de *Más información*.

Añadir un nuevo ítem a más información solo debemos clicar en el botón **Crear nueva página** y rellenar los campos.

Es muy importante que activemos el check de **Mostrar en la página de ayuda** si queremos mostrarlo en *Más Información*.

Para que se muestre debe estar en estado de **Publicada** y es importante rellenar el **Slug** también.

## Personalizar imágenes

Aunque ya se ha realizado la personalización de estas imágenes con las dimensiones correctas, desde **Contenido del sitio > Personalizar imágenes** es posible cambiar las imágenes como logotipos etc.

## Presupuestos Participativos

### Apoyos necesarios para pasar a la siguiente fase

Si la propuesta obtiene el número de apoyos necesarios se avisará a los usuarios que ya no necesita más para poder pasar a la siguiente fase.

En **Presupuestos participativos > "Presupuesto X" > Editar > "Partida X" > Editar** se podrán marcar las las partidas con los apoyos necesarios para distinguir entre distrito y pedanía.

### Votos negativos

Para la fase de votaciones, desde **Presupuestos participativos > "Presupuesto X" > Editar > Editar presupuesto** podremos definir la cantidad de votos negativos que puede asignar un usuario y su valor, para ser descontado del total.

### Sobre-escribir estadísticas

Para la fase de resultados, desde **Presupuestos participativos > "Presupuesto X" > Editar > Editar presupuesto** podremos sobre-escribir las estadísticas automáticas de Consul con nuestro HTML personalizado.

Al activar esta opción se nos abrirá un editor de texto. Lo recomendable trabajar en ello antes de marcar el checkbox de *Mostrar estadísticas*, para que no se muestre. También es recomendable copiar el HTML de un presupuesto anterior para utilizarlo como base e ir modificando los datos.

Las estadísticas ya incluidas se han diseñado para facilitar la inserción independientemente de los conocimientos que tenga, trabajando con tablas.

### Extensión de resultados

Para la fase de resultados, desde **Presupuestos participativos > "Presupuesto X" > Editar > Editar presupuesto** podremos añadir contenido adicional tras las tablas con los resultados. Esta parte es útil para incluir información adicional sobre reequilibrio territorial o poner un enlace a algún descargable.

### Proyectos de gasto

En **Presupuestos participativos > "Presupuesto X" > Proyectos de gasto** para la comodidad a la hora de las consultas del estado de los proyectos hemos incluido pestañas filtradas con la información más importante.

### Marcar ganadores de forma manual

Al hacer la mayoría de los cálculos fuera de Consul, hemos añadido el botón de *Indicar manualmente* en el que cargaremos un CSV con los ID-s de los proyectos ganadores.

Para ello debemos estar en la fase de *Votación finalizada*. En **Presupuestos participativos > "Presupuesto X" > Proyectos de gasto > Pestaña: Ganadores** encontraremos el botón para esto.
