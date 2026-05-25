load Rails.root.join("app", "controllers", "admin", "budget_investments_controller.rb")

class Admin::BudgetInvestmentsController
  has_filters %w[all without_admin without_valuator under_valuation valuation_finished enough_support not_enough_support winners],
              only: :index

  before_action :load_counters, only: [:index]

  def index
    load_tags
    respond_to do |format|
      format.html
      format.csv do
        send_data Budget::Investment::Exporter.new(@investments).to_csv,
                  filename: "budget_investments.csv"
      end
      format.xlsx do
        response.headers["Content-Disposition"] = 'attachment; filename="Propuestas de inversión.xlsx"'
      end
    end
  end

  private

    def load_investments
      # Override the method to allow xlsx export without pagination
      @investments = Budget::Investment.scoped_filter(params, @current_filter).order_filter(params)
      @investments = Kaminari.paginate_array(@investments) if @investments.is_a?(Array)
      @investments = @investments.page(params[:page]) unless request.format.csv? || request.format.xlsx?
    end

    def load_counters
      @counts = Budget::Investment.scoped_filter(params, @current_filter)
      @counts_total = @counts.count
      @counts_without_admin = @counts.where(administrator_id: nil).count
      @counts_without_val = @counts.where(valuator_assignments_count: 0).count
      @counts_in_val = @counts.where(valuation_finished: false).count
      @counts_aval_finished = @counts.where(valuation_finished: true).count
      @counts_enough_support = @counts.enough_support.count
      @counts_not_enough_support = @counts.not_enough_support.count
      @counts_winners = @counts.where(winner: true).count
    end
end
