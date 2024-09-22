from twisted.internet import reactor, protocol
import random
import json
import time

from dataclasses import dataclass


@dataclass
class ClimateData:
    temperatura: float
    umidade: float
    pressao: float

    def to_dict(self) -> dict:
        return {
            "temperatura": self.temperatura,
            "umidade": self.umidade,
            "pressao": self.pressao,
        }


def generate_climate_date() -> ClimateData:
    temperatura = round(random.uniform(20, 30), 1)  # Gera temperatura entre 20 e 30°C
    umidade = round(random.uniform(40, 70), 1)  # Gera umidade entre 40% e 70%
    pressao = round(
        random.uniform(1000, 1050), 1
    )  # Gera pressão entre 1000 hPa e 1050 hPa

    climate_data = ClimateData(
        temperatura=temperatura, umidade=umidade, pressao=pressao
    )

    return climate_data


class ClimateDataProtocol(protocol.Protocol):
    def connectionMade(self):
        print("Cliente conectado. Iniciando envio de dados...")
        self.sendData()

    def sendData(self):
        climate_data = generate_climate_date()

        data = climate_data.to_dict()
        data["tempo"] = time.time()

        self.transport.write(json.dumps(data).encode("utf-8") + b"\n")

        reactor.callLater(5, self.sendData)


class ClimateDataFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return ClimateDataProtocol()


PORT = 3000

reactor.listenTCP(PORT, ClimateDataFactory())
print(f"Servidor de dados climáticos rodando na porta {PORT}...")
reactor.run()
