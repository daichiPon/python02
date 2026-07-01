#!/usr/bin/env python3
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        100 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 10


def test_error_types() -> None:
    operations_arr = [0, 1, 2, 3, 4]
    for i in operations_arr:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()
    print()
    print("All error types tested successfully!")
