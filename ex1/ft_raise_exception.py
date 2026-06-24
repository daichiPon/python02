def input_temperature(temp_str:str) -> int:
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    if 0 > temp_int:
        raise ValueError(f"{temp_int}°C is too hot for plants (min 0°C)")
    return temp_int

def test_temperature() -> None:
    def test(temp_str:str)-> None:
        try:
            temp_int = input_temperature(temp_str)
            print(f"Temperature is now {temp_int}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    
    print("=== Garden Temperature Checker ===")
    print()
    temp_int = 25
    print(f"Input data is '{temp_int}'")
    test(temp_int)
    temp_str = "abs"
    print(f"Input data is '{temp_str}'")
    test(temp_str)
    temp_int = 100
    print(f"Input data is '{temp_int}'")
    test(temp_int)
    temp_int = -50
    print(f"Input data is '{temp_int}'")
    test(temp_int)
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()