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


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    def test(vegetables: list[str]) -> None:
        print("Opening watering system")
        try:
            for v in vegetables:
                water_plant(v)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system")

    vegetables: list[str] = [
        "Tomato",
        "Lettuce",
        "Carrots"
    ]
    invalid_vegetables: list[str] = [
        "Tomato",
        "lettuce",
        "Carrots"
    ]
    print("Testing valid plants...")
    test(vegetables)
    print()
    print("Testing invalid plants...")
    test(invalid_vegetables)


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
