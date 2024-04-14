import unittest
from src.motor import Motor
from src.chasis import Chasis, TipoChasis
from src.carroceria import Carroceria, TipoCarroceria
from src.llanta import Llanta
from src.asiento import Asiento
from src.carro import Carro

class TestCarComponents(unittest.TestCase):

    def test_motor(self):
        motor = Motor(2)
        self.assertEqual(motor.to_string(), "Motor: 2 litros")

    def test_chasis(self):
        chasis = Chasis(TipoChasis.MONOCASCO)
        self.assertEqual(chasis.to_string(), "Chasis: Monocasco")

    def test_carroceria(self):
        carroceria = Carroceria(TipoCarroceria.TUBULAR, "rojo")
        self.assertEqual(carroceria.to_string(), "Carrocería: Tubular, Color: rojo")

    def test_llanta(self):
        llanta = Llanta("Goodyear", 25, 20, 15)
        self.assertEqual(llanta.to_string(), "Llanta: Marca Goodyear, Rin 25 pulgadas, Altura 20 pulgadas, Anchura 15 pulgadas")

    def test_asiento(self):
        asiento = Asiento("cuero", True)
        self.assertEqual(asiento.to_string(), "Asiento de cuero, Funda: Sí")

    def test_carro_full_equipo(self):
        motor = Motor(2)
        chasis = Chasis(TipoChasis.MONOCASCO)
        carroceria = Carroceria(TipoCarroceria.TUBULAR, "rojo")
        llantas = [Llanta("Goodyear", 25, 20, 15) for _ in range(4)]
        asientos = [Asiento("cuero", True), Asiento("cuero", True), Asiento("tela", False)]
        full_equipo = {
            "Airbags": "Sí",
            "Frenos ABS": "Sí",
            "Vidrios eléctricos": "Sí",
            "Espejos eléctricos": "Sí",
            "Sunroof": "Sí"
        }
        carro = Carro(motor, chasis, carroceria, llantas, asientos, full_equipo)
        expected_info = "\n".join([
            "Motor: 2 litros",
            "Chasis: Monocasco",
            "Carrocería: Tubular, Color: rojo",
            "Llanta: Marca Goodyear, Rin 25 pulgadas, Altura 20 pulgadas, Anchura 15 pulgadas",
            "Llanta: Marca Goodyear, Rin 25 pulgadas, Altura 20 pulgadas, Anchura 15 pulgadas",
            "Llanta: Marca Goodyear, Rin 25 pulgadas, Altura 20 pulgadas, Anchura 15 pulgadas",
            "Llanta: Marca Goodyear, Rin 25 pulgadas, Altura 20 pulgadas, Anchura 15 pulgadas",
            "Asiento de cuero, Funda: Sí",
            "Asiento de cuero, Funda: Sí",
            "Asiento de tela, Funda: No",
            "Airbags: Sí",
            "Frenos ABS: Sí",
            "Vidrios eléctricos: Sí",
            "Espejos eléctricos: Sí",
            "Sunroof: Sí"
        ])
        self.assertEqual(carro.to_string(), expected_info)

if __name__ == '__main__':
    unittest.main()

#Comando para iniciar pruebas unitarias en el terminal
#python -m unittest discover -s tests
