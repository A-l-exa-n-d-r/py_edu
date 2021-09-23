"""
создайте класс `Car`, наследник `Vehicle`
"""
from .base import Vehicle
from .engine import Engine


class Car(Vehicle):
    engine = None

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)

    def set_engine(self, engine: Engine):
        self.engine = engine

