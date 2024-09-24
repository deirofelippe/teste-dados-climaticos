from twisted.internet import reactor, protocol
from netcdf_file import save_data, get_all_variables
from graphics import create_plot
import json


class ClimateDataReceiver(protocol.Protocol):
    def dataReceived(self, data):
        try:
            raw_data = data.decode("utf-8").strip()
            climate_data = json.loads(raw_data)

            print("==============================")
            print("Dados recebidos:")
            print(f"Tempo: {climate_data['tempo']}")
            print(f"Temperatura: {climate_data['temperatura']} °C")
            print(f"Umidade: {climate_data['umidade']} %")
            print(f"Pressão: {climate_data['pressao']} hPa")
            print("==============================")

            self.processData(climate_data)
        except Exception as e:
            print(f"Erro ao processar dados: {e}")

    def processData(self, data):
        print("Salvando dados...")
        save_data(
            tempo=data["tempo"],
            temperatura=data["temperatura"],
            umidade=data["umidade"],
            pressao=data["pressao"],
        )

        print("Buscando dados...")
        climate_date = get_all_variables()

        print("Criando plot...")
        create_plot(climate_date)


class ClimateDataFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        print("Conectado ao servidor de dados climáticos.")
        return ClimateDataReceiver()

    def clientConnectionFailed(self, connector, reason):
        print("Conexão falhou:", reason)
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Conexão perdida:", reason)
        reactor.stop()


PORT = 3000

reactor.connectTCP("app-dados", PORT, ClimateDataFactory())
reactor.run()
