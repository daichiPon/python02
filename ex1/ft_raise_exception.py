#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    return temp_int


def test_temperature() -> None:
    def test(temp_str: str) -> None:
        try:
            temp_int = input_temperature(temp_str)
            print(f"Temperature is now {temp_int}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("=== Garden Temperature Checker ===")
    print()
    print("Input data is '25'")
    test("25")
    print()
    print("Input data is 'abc'")
    test("abc")
    print()
    print("Input data is '100'")
    test("100")
    print()
    print("Input data is '-50'")
    test("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
