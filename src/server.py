from twisted.internet import reactor, protocol
import json

from generate_climate_date import generate_climate_date


class ClimateDataProtocol(protocol.Protocol):
    def connectionMade(self):
        print("Cliente conectado. Iniciando envio de dados...")
        self.sendData()

    def sendData(self):
        climate_data = generate_climate_date()

        data = climate_data.to_dict()

        self.transport.write(json.dumps(data).encode("utf-8") + b"\n")

        reactor.callLater(5, self.sendData)


class ClimateDataFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return ClimateDataProtocol()


PORT = 3000

reactor.listenTCP(PORT, ClimateDataFactory())
print(f"Servidor de dados climáticos rodando na porta {PORT}...")
reactor.run()
