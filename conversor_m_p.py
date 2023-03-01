COMMAND_NAME = "convmp"


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=float)
    parser.add_argument("operation", type=str, choices=["infeet", "inmeters"])

    args = parser.parse_args()

    value = args.value
    operation = args.operation

    calc_and_print(value, operation)


def calc_and_print(val: float | int, op: str) -> None:
    val = float(val)
    if op == "empes":
        final_val = round(val * 3.28084, 2)

    elif op == "emmetros":
        final_val = round(val / 3.28084, 2)

    else:
        raise ValueError("Invalid input")

    print(final_val)


if __name__ == "__main__":
    main()
else:
    command_name = "convmp"
    command_func = calc_and_print
    util_args = {"val": float, "op": str}
