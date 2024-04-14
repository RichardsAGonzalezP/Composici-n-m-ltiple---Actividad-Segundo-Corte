# src/carro.py

from src.motor import Motor
from src.chasis import Chasis
from src.carroceria import Carroceria
from src.llanta import Llanta
from src.asiento import Asiento


class Carro:
    def __init__(self, motor, chasis, carroceria, llantas, asientos, full_equipo):
        self.motor = motor
        self.chasis = chasis
        self.carroceria = carroceria
        self.llantas = llantas
        self.asientos = asientos
        self.full_equipo = full_equipo  # Diccionario con elementos de full equipo

    def to_string(self):
        carro_info = [
            self.motor.to_string(),
            self.chasis.to_string(),
            self.carroceria.to_string(),
            *map(lambda x: x.to_string(), self.llantas),
            *map(lambda x: x.to_string(), self.asientos),
            *[f"{key}: {value}" for key, value in self.full_equipo.items()]
        ]
        return "\n".join(carro_info)

