(function() {
  "use strict";
  App.ValuationBudgetInvestmentForm = {
    showFeasibleFields: function() {
      $("#valuation_budget_investment_edit_form #unfeasible_fields").hide("down");
      $("#valuation_budget_investment_edit_form #feasible_fields").show();
      App.ValuationBudgetInvestmentForm.showPhases();
      App.ValuationBudgetInvestmentForm.showPhasesOnChange();
    },
    showNotFeasibleFields: function() {
      $("#valuation_budget_investment_edit_form #feasible_fields").hide("down");
      $("#valuation_budget_investment_edit_form #unfeasible_fields").show();
    },
    showAllFields: function() {
      $("#valuation_budget_investment_edit_form #feasible_fields").show("down");
      $("#valuation_budget_investment_edit_form #unfeasible_fields").show("down");
    },
    showFeasibilityFields: function() {
      var feasibility;
      feasibility = $(
        "#valuation_budget_investment_edit_form input[type=radio]" +
        "[name='budget_investment[feasibility]']:checked"
      ).val();
      if (feasibility === "feasible") {
        App.ValuationBudgetInvestmentForm.showFeasibleFields();
      } else if (feasibility === "unfeasible") {
        App.ValuationBudgetInvestmentForm.showNotFeasibleFields();
      }
    },
    showFeasibilityFieldsOnChange: function() {
      $(
        "#valuation_budget_investment_edit_form input[type=radio]" +
        "[name='budget_investment[feasibility]']"
      ).on("change", function() {
        App.ValuationBudgetInvestmentForm.showAllFields();
        App.ValuationBudgetInvestmentForm.showFeasibilityFields();
      });
    },
    showPhases: function() {
      if ($("#budget_investment_allows_phase").prop("checked")) {
        $("#fases").show();
      } else {
        $("#fases").hide();
      }
    },
    showPhasesOnChange: function() {
      $("#budget_investment_allows_phase").on("change", function() {
        App.ValuationBudgetInvestmentForm.showPhases();
      });
    },
    initialize: function() {
      App.ValuationBudgetInvestmentForm.showFeasibilityFields();
      App.ValuationBudgetInvestmentForm.showFeasibilityFieldsOnChange();
    }
  };
}).call(this);
