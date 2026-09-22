(function() {
  "use strict";
  App.AdminSiteCustomizationPagesOrder = {
    initialize: function() {
      $(".more-info-pages-order-table tbody").sortable({
        update: function() {
          var new_order;
          new_order = $(this).sortable("toArray", {
            attribute: "data-page-id"
          });
          $.ajax({
            url: $(this).data("js-url"),
            data: {
              ordered_list: new_order
            },
            type: "POST"
          });
        }
      });
    }
  };
}).call(this);
