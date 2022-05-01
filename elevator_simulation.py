from __future__ import annotations
from typing import Callable

import numpy as np
import numpy.typing as npt

CURRENT_TIME: float = 0.0  # current time in seconds


class Person:
    target_floor: int

    def __init__(self) -> None:
        # On creation set target floor
        pass

    def get_next_action(self):
        pass


class Elevator:
    current_floor: int

    def __init__(self) -> None:
        pass

    def get_next_action(self):
        pass


class AllElevators:
    elevators: list[Elevator]

    def __init__(self, elevators: int) -> None:
        self.elevators = [Elevator() for _ in range(elevators)]

    def get_next_action(self):
        pass


class WaitingRoom:
    def __init__(self) -> None:
        pass


class Floor:
    waiting_room: WaitingRoom
    at_floor: WaitingRoom

    def __init__(self) -> None:
        self.waiting_room = WaitingRoom()
        self.at_floor = WaitingRoom()

    def get_next_action(self):
        pass


class Building:
    floors: list[Floor]
    elevators: AllElevators
    generator_function: Callable[[], float]

    def __init__(
        self,
        floors: int,
        elevators: int,
        generator_function: Callable[[], float],
    ) -> None:
        self.floors = [Floor() for _ in range(floors)]
        self.elevators = AllElevators(elevators)
        self.generator_function = generator_function

    def get_next_action(self):
        pass

    def simulate(self):
        pass


def exponential_generator():
    return np.random.exponential(20)


def main():
    building = Building(5, 2, exponential_generator)
    print(building.floors, building.elevators)


if __name__ == "__main__":
    main()
