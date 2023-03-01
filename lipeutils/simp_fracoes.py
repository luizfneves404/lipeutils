def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("numerator", type=int)
    parser.add_argument("denominator", type=int)

    args = parser.parse_args()

    numerator = args.numerator
    denominator = args.denominator

    calc_and_print(numerator, denominator)


# maximum common denominator
def mdc(num1: int, num2: int) -> int:
    divisor = min(num1, num2)
    while divisor > 1:
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
        else:
            divisor -= 1

    return 1


def calc_and_print(numer: int, denomin: int) -> None:
    mdc_of_fraction = mdc(numer, denomin)
    new_numer = numer / mdc_of_fraction
    new_denomin = denomin / mdc_of_fraction
    simplified_fraction = (int(new_numer), int(new_denomin))
    print(f"{simplified_fraction[0]}/{simplified_fraction[1]}")


if __name__ == "__main__":
    main()
else:
    command_name = "simp"
    command_func = calc_and_print
    util_args = {"numer": int, "denomin": int}
