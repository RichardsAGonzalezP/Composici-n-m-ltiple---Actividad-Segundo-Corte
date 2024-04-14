# main.py

from src.motor import Motor
from src.chasis import Chasis, TipoChasis
from src.carroceria import Carroceria, TipoCarroceria
from src.llanta import Llanta
from src.asiento import Asiento
from src.carro import Carro

def main():
    # Creación del motor con volumen de 2 litros
    motor = Motor(2)

    # Creación del chasis con tipo 'MONOCASCO'
    chasis = Chasis(TipoChasis.MONOCASCO)

    # Creación de la carrocería de tipo 'TUBULAR' y color 'rojo'
    carroceria = Carroceria(TipoCarroceria.TUBULAR, "rojo")

    # Creación de las cuatro llantas, todas con las mismas especificaciones
    llantas = [Llanta("Goodyear", 25, 20, 15) for _ in range(4)]

    # Creación de tres asientos, dos de cuero con funda y uno de tela sin funda
    asientos = [
        Asiento("cuero", True),  # Asiento del conductor con funda
        Asiento("cuero", True),  # Asiento del acompañante con funda
        Asiento("tela", False)   # Asiento trasero sin funda
    ]

    # Elementos adicionales del full equipo del carro
    full_equipo = {
        "Airbags": "Sí",
        "Frenos ABS": "Sí",
        "Vidrios eléctricos": "Sí",
        "Espejos eléctricos": "Sí",
        "Sunroof": "Sí"
    }

    # Creación del carro con todos los componentes
    carro = Carro(motor, chasis, carroceria, llantas, asientos, full_equipo)

    # Impresión de todos los detalles del carro
    print(carro.to_string())

if __name__ == '__main__':
    main()
