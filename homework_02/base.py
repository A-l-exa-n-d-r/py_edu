from abc import ABC
from .exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 1000
    started = False
    fuel = 100
    fuel_consumption = 1

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """
        перетаскивает состояние started в True, при наличии не отрицательного fuel
        """
        if not self.started:      # По ТЗ есть, но пока нет логики "запуска" - можно спокойно утилизировать проверку 🦆
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        """
        тратит fuel на прохождение distance, в зависимости от fuel_consumption, запрещает попытки исчерпать остаток fuel
        """
        fuel_need = distance * self.fuel_consumption
        if fuel_need <= self.fuel:
            self.fuel -= fuel_need
        else:
            raise NotEnoughFuel




