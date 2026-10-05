# Personalización para versión 2025-2026

## Frontend

### Encabezado

Aunque el texto y traducción proviene del **Encabezado** del **Administrador** de la **Homepage**; para poder añadir una imagen de fondo diferente según el **idioma** y para **desktop/mobile** se ha realizado los siguientes cambios:

- En `app/assets/images/custom`se ha añadido la carpeta `header` y las imágenes:
  - header_es.png
  - header_val.png
  - header_sm_es.png
  - header_sm_val.png
- En `app/custom/shared/_header.html.erb` podéis encontrar un nuevo código para `custom-header-card` donde se muestra la imagen según el idioma.
- Y en `app/assets/stylesheets/custom.scss` damos estilos para que se vea así.

#### Para recuperar el header original de Consul

Solo hace falta eliminar `app/custom/shared/_header.html.erb`. También puedes aprovechar para limpiar `app/assets/images/custom/header` y `app/assets/stylesheets/custom.scss`.

### Home: 3 tarjetas

Al igual que con el encabezado las **Tarjetas** o columnas de la **Homepage** las gestionamos desde el propio **Administrador** pero las imágenes tienen diferentes versiones según el **idioma**. Para diferenciarlos hemos utilizado las etiquetas de cada tarjeta:

- **crea**
- **elige**
- **vota**

Para ello en el código hemos hecho lo siguiente:

- En `app/assets/images/custom` se ha añadido la carpeta `columns` y las imágenes:
  - crea_es.jpg
  - crea_val.jpg
  - elige_es.jpg
  - elige_val.jpg
  - vota_es.jpg
  - vota_val.jpg
- En `app/custom/shared/` hemos creado `_cardshome.html.erb`y `_cardhome.html.erb` en vez de sustituir lo existente.
  - `app/custom/welcome/index.html.erb` llama a `cardshome`:

```bash
<%= render "shared/cardshome", cards: @cards %>
```

- `cardshome` llama a `cardhome`:

```bash
<%= render "shared/cardhome", card: card %>
```

- Y `cardhome` consulta el `card.label` para mostrar una imagen u otra.

```bash
  <%= link_to card.link_url do %>
    <% if card.label == "crea" %>
      <figure class="figure-card">
        <%= image_tag(image_path_for("columns/crea_#{locale}.jpg"), alt: card.title) %>
      </figure>
    <% elsif card.label == "elige" %>
      <figure class="figure-card">
        <%= image_tag(image_path_for("columns/elige_#{locale}.jpg"), alt: card.title) %>
      </figure>
    <% elsif card.label == "vota" %>
      <figure class="figure-card">
        <%= image_tag(image_path_for("columns/vota_#{locale}.jpg"), alt: card.title) %>
      </figure>
    <% else %>
      <figure class="figure-card">
        <% if card.image.present? %>
          <%= image_tag(card.image.variant(:large), alt: card.image.title) %>
        <% end %>
      </figure>
    <% end %>
```

#### Para recuperar las tarjetas de la homepage originales de Consul

Solo haría falta poner `"shared/cards"` en vez de `"shared/cardshome"` en `app/custom/welcome/index.html.erb`. También puedes eliminar `app/custom/shared/_cardshome.html.erb`y `app/custom/shared/_cardhome.html.erb`. Como todo lo que hay en la carpeta `app/assets/images/custom/columns`

### Presupuestos Participativos 2015/2016

Este apartado es una **página personalizada** del **Administrador** pero para incluirlo con el resto resultados de los presupuestos participativos se han hecho los siguientes cambios:

- Se ha creado `app/views/custom/budgets/_finished.html.erb` en donde al final incluimos el enlace a la página.
- El texto y el enlace son estáticos y se controlan desde cada idioma como `config/locales/custom/es/budgets.yml`.

```bash
    finished_budgets:
      2015_2016_title: "Presupuestos Participativos 2015/2016"
      2015_2016_link: "/budget-2015-2016"
```

#### Para recuperar el listado de presupuestos finalizados originales de Consul

Con eliminar `app/views/custom/budgets/_finished.html.erb` sería suficiente, aunque podemos limpiar los `.yml` también, e incluso eliminar la página personalizada.

### Fases con iconos propios

En `app/components/custom/budgets` se ha copiado `phases_component.html.erb` y en él hemos incluido el siguiente código:

```bash
  <%# CUSTOM phase-icon %>
    <div class="phase-icon">
      <%= image_tag(image_path_for("phases/#{phase.kind}_#{I18n.locale}.png")) %>
    </div>
  <%# //CUSTOM %>
```

En `app/assets/images/custom` se ha añadido la carpeta `phases` y las imágenes por idioma:

- accepting_x.png
- balloting_x.png
- finished_x.png
- informing_x.png
- publishing_prices_x.png
- reviewing_ballots_x.png
- selecting_x.png
- valuating_x.png

Solo debemos sustituir las imágenes si queremos mantener algún tipo de icono.

#### Para recuperar las fases originales de Consul

Con eliminar `app/views/custom/budgets/phases_component.html.erb` sería suficiente.

### Eliminar autor en detalle de proyectos de gastos

En `app/components/custom/shared` hemos traido los siguientes archivos:

- detailed_author_info_component.html.erb
- detailed_author_info_component.rb
- detailed_info_component.html.erb
- detailed_info_component.rb

En `detailed_author_info_component.html.erb` solo dejamos el colectivo. Y en `etailed_info_component.html.erb` cambiamos el orden.

#### Para que vuelva a mostrar el autor del proyecto de gasto de Consul

Con eliminar estos archivos sería suficiente.

### Cambiar orden de "Observaciones a la propuesta de inversión"

En `app/components/custom/budgets/investments` hemos traido los archivos `investment_detail_component.html.erb` y `investment_detail_component.rb`. Hemos cambiado el orden de `investment_code` y `price_explanation`.

Y desde el propio Administrador (`Contenido del sitio > Personalizar textos > Presupuestos participativos`) hemos cambiado el texto de "Informe de coste" por "Observaciones a la propuesta de inversión" en la variable `budgets.investments.show.price_explanation`

#### Para que vuelva a mostrar el orden anterior en Consul

Con eliminar estos archivos sería suficiente. Y en Personalizar textos volver a poner el texto original.

### Apartado "Más información" con desplegables (help)

Para poder desarrollar una página de **Más información** con desplegables, a modo de faq, hemos adaptado la página de `help`.

En el **Administrador** a la hora de añadir el contenido que queremos que se muestre en **Más información** debemos marcarlo para **Mostrar en la página de ayuda** y automáticamente aparecerá en formato desplegable.

Para ello, en `app/views/custom/pages/help` hemos editado `index.html.erp` para que no muestre el menú y la parte de `_other.html.erp` para convertirlo a `accordion` de `Foundation.

#### Para recuperar el help original de Consul

Al eliminar `app/views/custom/pages/help` volvería a funcionar el original.

### Etiqueta "Seleccionada por mecanismo de garantía."

En `app/views/custom/results/_results_table.html.erb` se ha incluido una etiqueta con el texto `budgets.results.territorial_rebalance` para los proyectos que coincidan con el ID marcado a mano en el propio documento.

```bash
  <%# Marcar las propuestas seleccionadas por reequibrio territorial %>
  <% rebalance_2022 = [6046, 6654, 5313, 6261, 6394, 6263, 6411, 6312, 6087, 5435, 6805, 6255, 6575, 6564, 5398]
      rebalance_2025 = [6046, 6654, 5313, 6261, 6394, 6263, 6411, 6312, 6087, 5435, 6805, 6255, 6575, 6564, 5398]
      rebalance = rebalance_2022 + rebalance_2025 %>
  <% if rebalance.include? investment.id %>
    <abbr title="<%= t("budgets.results.territorial_rebalance") %>" class="adjust-investments-advice-mark"> * </abbr>
    <div id="<%= dom_id(investment) %>_advice" class="adjust-investments-advice">
      <span>* <%= t("budgets.results.territorial_rebalance") %></span>
    </div>
  <% end %>
```

## Backend

### Ordernar páginas de help con drag and drop

Ahora que las páginas de `help` se utilizan para el apartado de Más Información en formato acordeón no encontramos con el problema de poder ordenarlos para que no fuera por fecha de creación.

- `db/migrate/20260921000000_add_position_to_site_customization_pages.rb`

### Descarga de excel personalizado con propuestas

En `app/views/custom/admin/budget_investments/index.xlsx.axlsx` tenemos la generación de un archivo excel con las columnas definidas por el ayuntamiento.

### SET WINNERS: poder subir CSV con los ganadores seleccionados manualmente

Una vez finalizadas las votaciones, además de poner calcular los ganadores automáticamente con Consul, hemos incluido un botón en la pestaña de ganadores para "Indicar manualmente" los ganadores. Subiendo un CSV con los IDs de estos.

En `app/controllers/custom/admin/budgets_controller.rb` se ha definido `set_winners`.

```bash
  def set_winners
```

### Votos en contra: Cantidad y valor

Ahora crear/editar un Presupuesto Participativo, podremos indicar la cantidad de votos negativos que puede dar el usuario y el valor de este.

Estos son los archivos modificados:

- `app/controllers/custom/admin/budgets_controller.rb`
- `app/controllers/custom/budgets/ballot/negativelines_controller.rb`
- `app/controllers/custom/management/budgets/ballot/negativelines_controller.rb`
- `app/models/custom/abilities/common.rb`
- `app/models/custom/budget/ballot/negativeline.rb`
- `app/models/custom/budget/ballot.rb`
- `app/models/custom/budget/investment.rb`
- `app/views/custom/admin/budget_investments/_investments.html.erb`
- `app/views/custom/admin/budgets/_form.html.erb`
- `app/views/custom/budgets/ballot/negativelines/_refresh_ballots.js.erb`
- `app/views/custom/budgets/ballot/negativelines/create.js.erb`
- `app/views/custom/budgets/ballot/negativelines/destroy.js.erb`
- `app/views/custom/budgets/ballot/_ballot.html.erb`
- `app/views/custom/budgets/ballot/_negativeinvestment.html.erb`
- `app/views/custom/budgets/ballot/_negativeinvestment_for_sidebar.html.erb`
- `app/views/custom/budgets/investments/_ballot.html.erb`
- `app/views/custom/budgets/investments/_header.html.erb`
- `app/views/custom/budgets/investments/_investment_sidebar.html.erb`
- `app/views/custom/budgets/investments/_sidebar.html.erb`
- `app/views/custom/budgets/investments/index.html.erb`
- `app/views/custom/budgets/results/_results_table.html.erb`
- `app/views/custom/management/budgets/ballot/negativelines/_refresh_ballots.js.erb`
- `app/views/custom/management/budgets/ballot/negativelines/create.js.erb`
- `app/views/custom/management/budgets/ballot/negativelines/destroy.js.erb`
- `app/views/custom/management/budgets/ballot/negativelines/new.js.erb`
- `config/routes/custom.rb`
- `db/migrate/20260413100032_add_budget_negative_votes.rb`

### Filtros personalizados en Proyectos de gastos

En los proyectos de gasto tenemos a modo de filtro las siguientes pestañas: **Sin administrador, Sin evaluador, En evaluación, Evaluación finalizada, Apoyos suficientes, Apoyos insuficientes y Ganadores**

- `app/models/custom/budget/investment.rb`