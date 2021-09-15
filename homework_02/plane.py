"""
создайте класс `Plane`, наследник `Vehicle`
"""
from .base import Vehicle
from .exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 20

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, loaded_cargo):
        new_cargo = self.cargo + loaded_cargo
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        be_cargo = self.cargo
        self.cargo = 0
        return be_cargo
