import random


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("num1", type=int)
    parser.add_argument("num2", type=int)
    parser.add_argument("num3", type=int)
    parser.add_argument("num4", type=int)
    parser.add_argument("num5", type=int)
    parser.add_argument("num6", type=int)

    args = parser.parse_args()

    args_list = list(vars(args).values())

    calc_and_print(*args_list)


def calc_and_print(
    num1: int, num2: int, num3: int, num4: int, num5: int, num6: int
) -> None:
    # create a guess_list variable containing a list of all the inputs
    guess_list = [num1, num2, num3, num4, num5, num6]

    # with a for loop, loop through the list, converting each item to integer
    for guess_num in range(len(guess_list)):
        guess_list[guess_num] = int(guess_list[guess_num])

    # check if inputted numbers are unique, so their frequency cannot be higher than 1
    for num in guess_list:
        if guess_list.count(num) > 1:
            # throw error; they are not unique
            raise ValueError("The numbers are not unique")

    # checking if inputted numbers are between 1 and 60
    for num in guess_list:
        if not (1 <= num <= 60):
            raise ValueError("The numbers are not between 1 and 60")

    correct_nums = random.sample(range(1, 61), 6)

    score = sum(num in correct_nums for num in guess_list)
    results = (score, correct_nums)
    if results[0] < 4:
        print("Sorry, but you didn't win anything.")

    elif results[0] == 4:
        print("You won a 'quadra'! That's amazing!")

    elif results[0] == 5:
        print("Congrats! You won a 'quinta'!!!")

    else:
        print("You won the mega-sena! Go ahead and take you millions.")

    print(
        f"The correct numbers were: {results[1][0]} {results[1][1]} {results[1][2]} {results[1][3]} {results[1][4]} {results[1][5]}"
    )


if __name__ == "__main__":
    main()
else:
    command_name = "mega"
    command_func = calc_and_print
    util_args = {
        "num1": int,
        "num2": int,
        "num3": int,
        "num4": int,
        "num5": int,
        "num6": int,
    }
