# src/chasis.py

class TipoChasis:
    INDEPENDIENTE = 'Independiente'
    MONOCASCO = 'Monocasco'

class Chasis:
    def __init__(self, tipo_chasis):
        self.tipo_chasis = tipo_chasis

    def to_string(self):
        return f"Chasis: {self.tipo_chasis}"
