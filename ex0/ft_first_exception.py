#!/usr/bin/env python3
def input_temperature(temp_str:str) -> int:
    return int(temp_str)

def test_temperature(temp_str:str) -> None:
    try:
        temp_int = input_temperature(temp_str)
        print(f"Temperature is now {temp_int}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: {e}")

if __name__ == "__main__" :
    print("=== Garden Temperature ===")
    print()
    temp_int = 24
    print(f"Input data is '{temp_int}'")
    test_temperature(temp_int)
    temp_str = "abs"
    print(f"Input data is '{temp_str}'")
    test_temperature(temp_str)
    print()
    print("All tests completed - program didn't crash!")