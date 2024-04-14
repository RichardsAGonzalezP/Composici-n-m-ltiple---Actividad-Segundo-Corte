# src/carroceria.py

class TipoCarroceria:
    INDEPENDIENTE = 'Independiente'
    AUTOPORTANTE = 'Autoportante'
    TUBULAR = 'Tubular'

class Carroceria:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def to_string(self):
        return f"Carrocería: {self.tipo}, Color: {self.color}"
