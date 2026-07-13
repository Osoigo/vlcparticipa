load Rails.root.join("app", "controllers", "budgets", "executions_controller.rb")

class Budgets::ExecutionsController
  alias_method :consul_show, :show

  def show
    consul_show
    respond_to do |format|
      format.html
      format.csv do
        data = CSV.generate() do |csv|
          csv << [
            "investment",
            "heading",
            "title",
            "url",
            "price",
            "status"
          ]
          @investments_by_heading.each do |heading, investments|
            investments.each do |investment|
              status = investment.milestones.published.with_status.order_by_publication_date.last&.status
              csv << [
                investment.id,
                heading.name,
                investment.title,
                polymorphic_url(investment, anchor: "tab-milestones"),
                investment.price,
                status.name
              ]
            end
          end
        end
        send_data data, filename: "executions.csv"
      end
    end
  end
end
