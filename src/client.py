from twisted.internet import reactor, protocol
import json

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt


def save(tempo, temperatura, umidade, pressao):
    # Cria um arquivo netCDF4
    dataset = Dataset("./dados_climaticos.nc", "w", format="NETCDF4_CLASSIC")

    # Dimensões (tempo)
    dataset.createDimension("tempo", None)

    # Variáveis
    tempos = dataset.createVariable("tempo", "f4", ("tempo",))
    temperaturas = dataset.createVariable("temperatura", "f4", ("tempo",))
    umidades = dataset.createVariable("umidade", "f4", ("tempo",))
    pressoes = dataset.createVariable("pressao", "f4", ("tempo",))

    # Dados simulados
    dados_tempo = np.array([0, 5, 10, 15, 20, 25, 30])  # Exemplo de tempos
    dados_temperaturas = np.array([25.3, 26.1, 24.8, 27.2, 28.0, 22.5, 23.9])
    dados_umidades = np.array([55.2, 57.6, 54.4, 60.1, 52.0, 48.3, 47.9])
    dados_pressoes = np.array([1012.1, 1009.8, 1015.2, 1010.5, 1008.7, 1013.6, 1014.4])

    # Escreve os dados no arquivo netCDF
    tempos[:] = tempo
    temperaturas[:] = temperatura
    umidades[:] = umidade
    pressoes[:] = pressao

    # Fecha o arquivo
    dataset.close()


def create_plot():
    # Dados de exemplo
    tempos = np.array([0, 5, 10, 15, 20, 25, 30])
    temperaturas = np.array([25.3, 26.1, 24.8, 27.2, 28.0, 22.5, 23.9])
    umidades = np.array([55.2, 57.6, 54.4, 60.1, 52.0, 48.3, 47.9])
    pressoes = np.array([1012.1, 1009.8, 1015.2, 1010.5, 1008.7, 1013.6, 1014.4])

    # Plotando a Temperatura
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(tempos, temperaturas, label="Temperatura (°C)", color="r")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Temperatura (°C)")
    plt.legend()

    # Plotando a Umidade
    plt.subplot(3, 1, 2)
    plt.plot(tempos, umidades, label="Umidade (%)", color="b")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Umidade (%)")
    plt.legend()

    # Plotando a Pressão
    plt.subplot(3, 1, 3)
    plt.plot(tempos, pressoes, label="Pressão (hPa)", color="g")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Pressão (hPa)")
    plt.legend()

    plt.tight_layout()
    plt.savefig("./figure.png")
    plt.show()


class ClimateDataReceiver(protocol.Protocol):
    def dataReceived(self, data):
        try:
            # Processando os dados recebidos (em JSON)
            raw_data = data.decode("utf-8").strip()
            climate_data = json.loads(raw_data)
            self.processData(climate_data)
        except Exception as e:
            print(f"Erro ao processar dados: {e}")

    def processData(self, data):
        # Aqui você pode processar os dados com NumPy, salvá-los ou apenas exibi-los
        save(
            tempo=data["tempo"],
            temperatura=data["temperatura"],
            umidade=data["umidade"],
            pressao=data["pressao"],
        )

        create_plot()

        print(f"Dados recebidos:")
        print(f"  Tempo: {data['tempo']}")
        print(f"  Temperatura: {data['temperatura']} °C")
        print(f"  Umidade: {data['umidade']} %")
        print(f"  Pressão: {data['pressao']} hPa")
        print("---")


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
