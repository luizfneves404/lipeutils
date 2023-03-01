import random


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("difficulty", type=int, choices=[1, 2, 3])
    parser.add_argument("guess", type=int)

    args = parser.parse_args()

    difficulty = args.difficulty
    guess = args.guess

    calc_and_print(difficulty, guess)


def calc_and_print(diff: int, guess: int) -> None:
    easy_lottery = Lottery(1, 10)
    medium_lottery = Lottery(1, 100)
    hard_lottery = Lottery(1, 1000)

    if diff == 1:
        guess_report = easy_lottery.try_guess(guess)

    elif diff == 2:
        guess_report = medium_lottery.try_guess(guess)

    else:  # difficulty is 3
        guess_report = hard_lottery.try_guess(guess)

    if guess_report[0]:
        print("Congratulations! You did it!")
    else:
        print(f"Sorry, not this time. It was {guess_report[1]}")


class Lottery:
    def __init__(self, lower_bound: int, upper_bound: int):
        if not (self.lower_bound <= lower_bound <= upper_bound <= self.upper_bound):
            raise ValueError("lower bound or upper bound must be natural numbers")

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def try_guess(self, guess: int):
        correct_num = random.randint(self.lower_bound, self.upper_bound)
        return (True, correct_num) if guess == correct_num else (False, correct_num)


if __name__ == "__main__":
    main()
else:
    command_name = "lot"
    command_func = calc_and_print
    util_args = {"diff": int, "guess": int}
