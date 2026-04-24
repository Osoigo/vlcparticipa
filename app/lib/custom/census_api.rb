load Rails.root.join("app", "lib", "census_api.rb")

class CensusApi
  class Response
    def valid?
      data.dig(:datos_habitante, :item, :fecha_nacimiento_string).present?
    end

    def gender
      case datos_habitante[:descripcion_sexo]
      when "Varón", "Hombre"
        "male"
      when "Mujer"
        "female"
      end
    end

    def datos_habitante
      data[:datos_habitante][:item]
    end

    def datos_vivienda
      data[:datos_vivienda][:item]
    end
  end

  private

    def get_response_body(document_type, document_number)
      if end_point_available?
        begin
          xml = build_xml_request(document_type: document_type, document_number: document_number)

          response = client.call(:get_habitante_by_dni, xml: xml)
          hash = Hash.from_xml(response.to_xml.gsub("\n", ""))
          build_compatible_response(hash)
        rescue Exception => e
          Rails.logger.error "Census API call failed: #{e.message}"
        end
      else
        stubbed_response(document_type, document_number)
      end
    end

    def client
      @client = Savon.client(wsdl: Rails.application.secrets.census_api_end_point,
                             element_form_default: :qualified,
                             ssl_verify_mode: :none)
    end

    def build_xml_request(document_type:, document_number:)
      api_username = Rails.application.secrets.census_api_username
      api_password = Rails.application.secrets.census_api_password
      api_token = Rails.application.secrets.census_api_token

      <<~XML
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v20="http://www.valencia.es/services/esb/padron/WSPadron/v20" xmlns:wsp="http://www.valencia.es/services/esb/padron/WSPadron">
          <soapenv:Header>
            <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
              <wsse:UsernameToken wsu:Id="UsernameToken-#{api_token}">
                <wsse:Username>#{api_username}</wsse:Username>
                <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">#{api_password}</wsse:Password>
              </wsse:UsernameToken>
            </wsse:Security>
          </soapenv:Header>
          <soapenv:Body>
            <v20:GetHabitanteByDNIRequest version="2.0" fileTransfer="MTOM">
              <wsp:TipoDocumento>#{document_type}</wsp:TipoDocumento>
              <wsp:Documentacion>#{document_number}</wsp:Documentacion>
              <wsp:Nivel>2</wsp:Nivel>
              <wsp:IncluyeBaja>false</wsp:IncluyeBaja>
            </v20:GetHabitanteByDNIRequest>
          </soapenv:Body>
        </soapenv:Envelope>
      XML
    end

    def end_point_available?
      (Rails.env.staging? || Rails.env.preproduction? || Rails.env.production?) && end_point_defined?
    end

    def stubbed_valid_response
      {
        get_habita_datos_response: {
          get_habita_datos_return: {
            hay_errores: false,
            datos_habitante: {
              item: {
                fecha_nacimiento_string: "31-12-1980",
                identificador_documento: "12345678Z",
                descripcion_sexo: "Hombre",
                nombre: "Jose María",
                apellido1: "Pérez",
                nia: "123456789",
                primer_apellido: "Pérez",
                segundo_apellido: "Martínez",
                municipio_nacimiento: "València",
                provincia_nacimiento: "València",
                pais_nacimiento: "España",
                nacionalidad: "ES",
                tipoDocumento: "DNI",
                documentacion: "12345678Z",
                letra: "Z",
                fecha_ultima_modificacion: "01-01-2024",
                fecha_alta_inscripcion: "01-01-2020",
                entidad_colectiva: "46",
                entidad_singular: "València",
                nucleo: "Ciutat Vella",
                codigo_unico_entidad: stubbed_postal_code,
                telefono: "600123456",
                nivel_instruccion: "Universitaria",
                fecha_caducidad_permiso: nil,
                habitante_protegido: false
              }
            },
            datos_vivienda: {
              item: {
                codigo_postal: stubbed_postal_code,
                codigo_distrito: "01",
                provincia: "València",
                municipio: "València",
                acronimo: "C/",
                tipovia: "Calle",
                nombreCalle: "Colón",
                numero: "10",
                kilometro: nil,
                escalera: "A",
                planta: "3",
                puerta: "2",
                direccion_planchada: "C/ Colón, 10, Esc. A, 3º 2ª, 46004 València",
                distrito: "01",
                seccion: "05",
                numero_hoja: "123"
              }
            }
          }
        }
      }
    end

    # Returns postal code from Madrid in the test environment so tests can pass.
    # In any other environment, it returns a postal code from Valencia.
    def stubbed_postal_code
      if Rails.env.test?
        "28013"
      else
        "46001"
      end
    end

    # Build response from the hash compatible with original implementation
    def build_compatible_response(hash)
      if hash.present?
        body = hash["Envelope"]["Body"]["GetHabitanteByDNIResponse"]["Habitante"]["DatosPersonales"] rescue {}
        direccion = body["Direccion"] || {}
        municipio_nacimiento = body["MunicipioNacimiento"] || {}
        provincia_nacimiento = body["ProvinciaNacimiento"] || {}
        nacionalidad = body["Nacionalidad"] || {}
        entidad_colectiva = body["EntidadColectiva"] || {}
        entidad_singular = body["EntidadSingular"] || {}
        nucleo = body["Nucleo"] || {}
        nivel_instruccion = body["NivelInstruccion"] || {}

        {
          get_habita_datos_response: {
            get_habita_datos_return: {
              hay_errores: false,
              datos_habitante: {
                item: {
                  fecha_nacimiento_string: body["FechaNacimiento"],
                  identificador_documento: body["Documentacion"],
                  descripcion_sexo: body["Sexo"],
                  nombre: body["Nombre"],
                  apellido1: body["PrimerApellido"],
                  nia: body["NIA"],
                  primer_apellido: body["PrimerApellido"],
                  segundo_apellido: body["SegundoApellido"],
                  municipio_nacimiento: municipio_nacimiento["Nombre"],
                  provincia_nacimiento: provincia_nacimiento["Nombre"],
                  pais_nacimiento: body["PaisNacimiento"],
                  nacionalidad: nacionalidad["Codigo"],
                  tipoDocumento: body["TipoDocumento"],
                  documentacion: body["Documentacion"],
                  letra: body["Letra"],
                  fecha_ultima_modificacion: body["FechaUltimaModificacion"],
                  fecha_alta_inscripcion: body["FechaAltaInscripcion"],
                  entidad_colectiva: entidad_colectiva["Codigo"],
                  entidad_singular: entidad_singular["Descripcion"],
                  nucleo: nucleo["Descripcion"],
                  codigo_unico_entidad: body["CodigoUnicoEntidad"],
                  telefono: body["Telefono"],
                  nivel_instruccion: nivel_instruccion["Descripcion"],
                  fecha_caducidad_permiso: body["FechaCaducidadPermiso"],
                  habitante_protegido: body["HabitanteProtegido"]
                }
              },
              datos_vivienda: {
                item: {
                  codigo_postal: direccion["CodigoPostal"],
                  codigo_distrito: body["Distrito"],
                  provincia: direccion["Provincia"]&.[]("Nombre"),
                  municipio: direccion["Municipio"]&.[]("Nombre"),
                  acronimo: direccion["Acronimo"],
                  tipovia: direccion["Tipovia"],
                  nombreCalle: direccion["NombreCalle"],
                  numero: direccion["Numero"],
                  kilometro: direccion["Kilometro"],
                  escalera: direccion["Escalera"],
                  planta: direccion["Planta"],
                  puerta: direccion["Puerta"],
                  direccion_planchada: direccion["DireccionPlanchada"],
                  distrito: body["Distrito"],
                  seccion: body["Seccion"],
                  numero_hoja: body["NumeroHoja"]
                }
              }
            }
          }
        }
      else
        stubbed_invalid_response
      end
    end
end
