# src/asiento.py

class Asiento:
    def __init__(self, material, tiene_funda):
        self.material = material
        self.tiene_funda = tiene_funda

    def to_string(self):
        return f"Asiento de {self.material}, Funda: {'Sí' if self.tiene_funda else 'No'}"
