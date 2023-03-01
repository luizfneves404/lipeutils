def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)

    args = parser.parse_args()

    day = args.day

    calc_and_print(day)


def calc_value(day: int) -> float:
    if day < 1:
        ValueError("Day must be positive")

    value = ((2 ** (day - 1)) * 2) - 1
    return value / 100


def calc_and_print(day: int) -> None:
    result = calc_value(day)
    print(f"{result} reais")


if __name__ == "__main__":
    main()
else:
    command_name = "ccc"
    command_func = calc_and_print
    util_args = {"day": int}
