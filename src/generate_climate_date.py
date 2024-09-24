import random
from dataclasses import dataclass
from typing import Optional
import time


@dataclass
class ClimateData:
    tempo: float | list[float]
    temperatura: float | list[float]
    umidade: float | list[float]
    pressao: float | list[float]

    def to_dict(self) -> dict:
        return {
            "tempo": self.tempo,
            "temperatura": self.temperatura,
            "umidade": self.umidade,
            "pressao": self.pressao,
        }


def generate_climate_date() -> ClimateData:
    tempo = time.time()
    temperatura = round(random.uniform(20, 30), 1)  # Gera temperatura entre 20 e 30°C
    umidade = round(random.uniform(40, 70), 1)  # Gera umidade entre 40% e 70%
    pressao = round(
        random.uniform(1000, 1050), 1
    )  # Gera pressão entre 1000 hPa e 1050 hPa

    climate_data = ClimateData(
        temperatura=temperatura, umidade=umidade, pressao=pressao, tempo=tempo
    )

    return climate_data
