require "rails_helper"

describe "Voter" do
  context "Origin", :with_frozen_time do
    let(:poll) { create(:poll) }
    let!(:question) { create(:poll_question, :yes_no, poll: poll, title: "Is this question stupid?") }
    let(:booth) { create(:poll_booth) }
    let(:officer) { create(:poll_officer) }
    let(:admin) { create(:administrator) }

    before do
      create(:geozone, :in_census)
      create(:poll_shift, officer: officer, booth: booth, date: Date.current, task: :vote_collection)
      create(:poll_officer_assignment, officer: officer, poll: poll, booth: booth)
    end

    scenario "Voting in poll and then verifying account" do
      allow_any_instance_of(Verification::Sms).to receive(:generate_confirmation_code).and_return("1357")
      user = create(:user)
      admin_user = admin.user

      login_through_form_as_officer(officer)
      vote_for_poll_via_booth

      logout
      login_as user
      visit account_path
      click_link "Verify my account"

      verify_residence

      visit poll_path(poll)

      within_fieldset "Is this question stupid?" do
        expect(page).to have_field "Yes", type: :radio, disabled: true
        expect(page).to have_field "No", type: :radio, disabled: true
      end

      expect(page).to have_content "You have already participated in a physical booth. " \
                                   "You can not participate again."

      logout
      login_as(admin_user)
      visit admin_poll_recounts_path(poll)

      within("#total_system") do
        expect(page).to have_content "1"
      end

      within "tr", text: booth.name do
        expect(page).to have_content "1"
      end
    end
  end
end
