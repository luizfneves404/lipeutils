def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("initial_value", type=float)
    parser.add_argument("rate", type=float)
    parser.add_argument("time", type=float)

    args = parser.parse_args()

    initial_value = args.initial_value
    rate = args.rate
    time = args.time

    calc_and_print(initial_value, rate, time)


def calc_and_print(value: float | int, rate: float | int, time: float | int) -> None:
    # convert all inputs to floats
    value, rate, time = float(value), float(rate), float(time)

    if rate <= 0 or time <= 0 or value <= 0:
        raise ValueError("rate, time and value must be positive")

    rate /= 100
    result = round((value * rate * time) + value, 2)
    print(result)


if __name__ == "__main__":
    main()
else:
    command_name = "cjs"
    command_func = calc_and_print
    util_args = {"value": float, "rate": float, "time": float}
