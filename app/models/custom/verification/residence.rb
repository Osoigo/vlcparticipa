load Rails.root.join("app", "models", "verification", "residence.rb")

class Verification::Residence
  validate :document_number_length

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
end
