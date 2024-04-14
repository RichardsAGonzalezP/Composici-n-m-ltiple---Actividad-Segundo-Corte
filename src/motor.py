# src/motor.py

class Motor:
    def __init__(self, volumen):
        self.volumen = volumen

    def to_string(self):
        return f"Motor: {self.volumen} litros"
