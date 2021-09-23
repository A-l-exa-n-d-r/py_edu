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
        """
        наполняет cargo указанным количеством loaded_cargo, при условии не превышения итога над max_cargo
        """
        cargo_needed = self.cargo + loaded_cargo
        if cargo_needed <= self.max_cargo:
            self.cargo = cargo_needed
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        """
        сбрасывает cargo в 0
        :return: сколько cargo было
        """
        be_cargo = self.cargo
        self.cargo = 0
        return be_cargo
