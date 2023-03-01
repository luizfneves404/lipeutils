def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str, choices=["+", "-", "*", "/"])
    parser.add_argument("num1", type=float)
    parser.add_argument("num2", type=float)

    args = parser.parse_args()

    operation = args.operation
    num1 = args.num1
    num2 = args.num2

    calc_and_print(operation, num1, num2)


def calc(operation: str, num1: float | int, num2: float | int) -> float:
    if operation not in ["+", "-", "*", "/"]:
        raise ValueError("Invalid operation")
    try:
        num1, num2 = float(num1), float(num2)
    except ValueError as e:
        raise ValueError("Invalid inputs") from e

    if operation == "*":
        return num1 * num2

    elif operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    else:
        return num1 / num2


def calc_and_print(operation: str, num1: float | int, num2: float | int) -> None:
    result = calc(operation, num1, num2)
    print(result)


if __name__ == "__main__":
    main()
else:
    command_name = "ca"
    command_func = calc_and_print
    util_args = {"operation": str, "num1": float, "num2": float}
