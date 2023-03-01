import math
from typing import Tuple


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)

    args = parser.parse_args()

    num = args.num

    calc_and_print(num)


def is_prime(num: int) -> Tuple[bool, None | int]:
    # throw error if num is less than 1
    if num < 1:
        raise ValueError("num must be greater than 0")

    if num == 1:
        return False, None
    if num == 2:
        return True, None

    divisor = 2

    if num % divisor == 0:
        return False, divisor

    divisor += 1
    while divisor <= math.sqrt(num):
        if num % divisor == 0:
            return False, divisor

        divisor += 2

    return True, None


def calc_and_print(number: int) -> None:
    prime_report = is_prime(number)
    if prime_report[0]:
        print("The number is prime")
    else:
        print(f"The number is not prime because at least {prime_report[1]} divides it.")


if __name__ == "__main__":
    main()
else:
    command_name = "prim"
    command_func = calc_and_print
    util_args = {"number": int}
