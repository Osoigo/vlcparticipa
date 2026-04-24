require "rails_helper"

describe CensusApi do
  let(:api) { CensusApi.new }
  let(:real_valid_response) do
    File.read(file_fixture("census_api/success_response.xml"))
  end

  describe "#call" do
    before do
      allow_any_instance_of(Savon::Client).to receive(:call).and_return(double(to_xml: real_valid_response))
      allow(api).to receive(:end_point_available?).and_return(true)
    end

    it "returns data from a real response" do
      response = api.call(1, "12345678Z")

      expect(response).to be_valid
      expect(response.name).to eq("JOSE MARÍA PÉREZ")
      expect(response.datos_vivienda[:direccion_planchada]).to eq("C/ Calle de ejemplo, 10, P03 002")
    end
  end
end
