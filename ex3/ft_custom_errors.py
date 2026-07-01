#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def test_error_plant() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_error_water() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_error_all() -> None:
    errors: list[GardenError] = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]

    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    test_error_plant()
    print()
    print("Testing WaterError...")
    test_error_water()
    print()
    print("Testing catching all garden errors...")
    test_error_all()
    print()
    print("All custom error types work correctly!")
