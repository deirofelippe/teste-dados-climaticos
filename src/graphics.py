from generate_climate_date import ClimateData
import matplotlib.pyplot as plt

PATH_FILE = "/home/jovyan/work/figure.png"


def create_plot(climate_date: ClimateData):
    data = climate_date.to_dict()

    tempo = data["tempo"]
    temperatura = data["temperatura"]
    umidade = data["umidade"]
    pressao = data["pressao"]

    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(tempo, temperatura, label="Temperatura (°C)", color="r")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Temperatura (°C)")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(tempo, umidade, label="Umidade (%)", color="b")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Umidade (%)")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(tempo, pressao, label="Pressão (hPa)", color="g")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Pressão (hPa)")
    plt.legend()

    plt.tight_layout()
    plt.savefig(PATH_FILE)
    plt.close()
