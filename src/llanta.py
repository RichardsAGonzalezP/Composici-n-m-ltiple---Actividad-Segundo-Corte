# src/llanta.py

class Llanta:
    def __init__(self, marca, diametro_rin, altura, anchura):
        self.marca = marca
        self.diametro_rin = diametro_rin
        self.altura = altura
        self.anchura = anchura

    def to_string(self):
        return f"Llanta: Marca {self.marca}, Rin {self.diametro_rin} pulgadas, Altura {self.altura} pulgadas, Anchura {self.anchura} pulgadas"
