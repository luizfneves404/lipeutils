def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("buy_price", type=float)
    parser.add_argument("sell_price", type=float)
    parser.add_argument("quantity", type=float)

    args = parser.parse_args()

    buy_price = args.buy_price
    sell_price = args.sell_price
    quantity = args.quantity

    calc_and_print(buy_price, sell_price, quantity)


def calc_and_print(
    initial_price: float | int, final_price: float | int, quantity: float | int
) -> None:
    initial_price, final_price, quantity = (
        float(initial_price),
        float(final_price),
        float(quantity),
    )
    # throw error if inputs are less than zero
    if initial_price <= 0 or final_price <= 0 or quantity <= 0:
        raise ValueError("Values must be positive")

    profit = (final_price - initial_price) * quantity
    profit_percentage = round((profit / (initial_price * quantity)) * 100, 2)

    profit_report = (profit, profit_percentage)

    print(f"{profit_report[0]}, which represents {profit_report[1]}% of the investment")


if __name__ == "__main__":
    main()
else:
    command_name = "cl"
    command_func = calc_and_print
    util_args = {"initial_price": float, "final_price": float, "quantity": float}
