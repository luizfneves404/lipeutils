def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("height", type=float)
    parser.add_argument("weight", type=float)

    args = parser.parse_args()

    height = args.height
    wheight = args.weight

    calc_and_print(height, wheight)


def calc_and_print(h: float, w: float) -> None:
    result = round(w / (h**2), 2)
    print(result)

    if result < 18:
        print("On the low end")

    elif result <= 24.9:
        print("On the ideal range")

    elif result <= 30:
        print("Overweight")

    else:
        print("Obese")


if __name__ == "__main__":
    main()
else:
    command_name = "cimc"
    command_func = calc_and_print
    util_args = {"height": float, "weight": float}
