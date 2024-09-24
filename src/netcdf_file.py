from netCDF4 import Dataset
from generate_climate_date import ClimateData
import numpy as np
import os

PATH_FILE = "/home/jovyan/work/dados_climaticos.nc"


def create_file():
    dataset = Dataset(PATH_FILE, "w", format="NETCDF4_CLASSIC")

    dataset.createDimension("tempo", None)

    dataset.createVariable("tempo", "f4", ("tempo",))
    dataset.createVariable("temperatura", "f4", ("tempo",))
    dataset.createVariable("umidade", "f4", ("tempo",))
    dataset.createVariable("pressao", "f4", ("tempo",))

    dataset.close()


def get_all_variables() -> ClimateData:
    if not os.path.exists(PATH_FILE):
        raise Exception("Arquivo não existe")

    dataset = Dataset(PATH_FILE, "r")

    try:
        tempo_var = dataset.variables["tempo"]
        temperatura_var = dataset.variables["temperatura"]
        umidade_var = dataset.variables["umidade"]
        pressao_var = dataset.variables["pressao"]

        climate_data = ClimateData(
            tempo=tempo_var[:].tolist(),
            pressao=pressao_var[:].tolist(),
            temperatura=temperatura_var[:].tolist(),
            umidade=umidade_var[:].tolist(),
        )
    except Exception as e:
        print(e)
        raise e
    finally:
        dataset.close()

    return climate_data


def save_data(tempo, temperatura, umidade, pressao):
    if not os.path.exists(PATH_FILE):
        print("Criando arquivo...")
        create_file()

    dataset = Dataset(PATH_FILE, "a")

    try:
        tempo_var = dataset.variables["tempo"]
        temperatura_var = dataset.variables["temperatura"]
        umidade_var = dataset.variables["umidade"]
        pressao_var = dataset.variables["pressao"]

        tempo_len = len(tempo_var[:])
        temperatura_len = len(temperatura_var[:])
        umidade_len = len(umidade_var[:])
        pressao_len = len(pressao_var[:])

        tempo_var[tempo_len:] = np.array([tempo])
        temperatura_var[temperatura_len:] = np.array([temperatura])
        umidade_var[umidade_len:] = np.array([umidade])
        pressao_var[pressao_len:] = np.array([pressao])
    except Exception as e:
        print(e)
        raise e
    finally:
        dataset.close()
