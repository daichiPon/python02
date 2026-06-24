class GardenError(Exception):
    def __init__(self,messege: str = "Unknown Garden error"):
        super().__init__(messege)
    
class PlantError(GardenError):
    def __init__(self,messege: str = "Unknown plant error"):
        super().__init__(messege)

class WaterError(GardenError):
    def __init__(self,messege: str = "Unknown Water error" ):
        super().__init__(messege)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    
def test_watering_system() -> None:
    def test(vegitable: list) -> None:
        print("Opening watering system")
        try:
            for v in vegitable:
                water_plant(v)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system")
            
    vegitable: list = [
        "Tomato",
        "Lettuce",
        "Carrots"
    ]
    e_vegitable: list = [
        "Tomato",
        "lettuce",
        "Carrots"
    ]
    print("Testing valid plants...")
    test(vegitable)
    print()
    print("Testing invalid plants...")
    test(e_vegitable)

if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")