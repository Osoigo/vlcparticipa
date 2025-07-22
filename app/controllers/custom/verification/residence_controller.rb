load Rails.root.join("app", "controllers", "verification", "residence_controller.rb")

class Verification::ResidenceController
  def create
    @residence = Verification::Residence.new(residence_params.merge(user: current_user))
    if @residence.save
      redirect_to account_path, notice: t("verification.residence.create.flash.success")
    else
      render :new
    end
  end
end
