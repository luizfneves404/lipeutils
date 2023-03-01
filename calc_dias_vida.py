import datetime


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    parser.add_argument("month", type=int)
    parser.add_argument("year", type=int)

    args = parser.parse_args()

    birth_day = args.day
    birth_month = args.month
    birth_year = args.year

    calc_and_print(birth_day, birth_month, birth_year)


def calc(
    day: int, month: int, year: int
) -> int:  # sourcery skip: aware-datetime-for-utc

    now = datetime.datetime.utcnow() - datetime.timedelta(hours=3)
    birth_date = datetime.datetime(year, month, day)

    return (now - birth_date).days


def calc_and_print(d: int, m: int, y: int) -> None:
    try:
        datetime.datetime(y, m, d)
    except ValueError:
        print("Invalid date")
        raise

    days_since = calc(d, m, y)
    print(f"{days_since} full days since you were born")


if __name__ == "__main__":
    main()
else:
    command_name = "cdv"
    command_func = calc_and_print
    util_args = {"day": int, "month": int, "year": int}
