"""Simple stock portfolio tracker.

User enters a stock symbol and quantity repeatedly.
The program checks prices from a hardcoded dictionary, totals the investment,
then optionally writes the result to a .txt or .csv file.
"""

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 335.00,
    "GOOGL": 130.00,
    "AMZN": 150.00,
}


def format_currency(amount):
    return f"${amount:,.2f}"


def get_stock_symbol():
    while True:
        symbol = input("Enter stock symbol (or press Enter to finish): ").strip().upper()
        if not symbol:
            return None
        if symbol in STOCK_PRICES:
            return symbol
        print(f"Unknown symbol '{symbol}'. Supported symbols: {', '.join(sorted(STOCK_PRICES))}.")


def get_quantity(symbol):
    while True:
        text = input(f"Enter quantity for {symbol}: ").strip()
        if not text:
            print("Quantity is required.")
            continue
        if not text.isdigit():
            print("Please enter a whole number for quantity.")
            continue
        quantity = int(text)
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
        return quantity


def ask_save_option():
    while True:
        choice = input("Save result to file? (y/n): ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False
        print("Please answer 'y' or 'n'.")


def ask_file_type():
    while True:
        choice = input("Choose file type ('txt' or 'csv'): ").strip().lower()
        if choice in {"txt", "csv"}:
            return choice
        print("Please enter 'txt' or 'csv'.")


def save_report(filename, lines):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    print(f"Saved results to {filename}")


def main():
    print("Stock Portfolio Tracker")
    print("Available stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: {format_currency(price)}")
    print()

    holdings = []
    while True:
        symbol = get_stock_symbol()
        if symbol is None:
            break
        quantity = get_quantity(symbol)
        holdings.append((symbol, quantity))
        print(f"Added {quantity} shares of {symbol}.\n")

    if not holdings:
        print("No holdings entered. Exiting.")
        return

    total_value = 0.0
    report_lines = ["Stock Portfolio Summary", "-----------------------"]
    report_lines.append(f"{'Symbol':<8}{'Qty':>6}{'Price':>12}{'Value':>14}")
    report_lines.append("" + "-" * 40)

    for symbol, quantity in holdings:
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_value += value
        report_lines.append(
            f"{symbol:<8}{quantity:>6}{format_currency(price):>12}{format_currency(value):>14}"
        )

    report_lines.append("" + "-" * 40)
    report_lines.append(f"Total investment value: {format_currency(total_value)}")

    print("\n".join(report_lines))

    if ask_save_option():
        file_type = ask_file_type()
        filename = f"stock_portfolio.{file_type}"
        if file_type == "csv":
            csv_lines = ["Symbol,Quantity,Price,Value"]
            for symbol, quantity in holdings:
                price = STOCK_PRICES[symbol]
                value = price * quantity
                csv_lines.append(f"{symbol},{quantity},{price:.2f},{value:.2f}")
            csv_lines.append(f"Total,,,{total_value:.2f}")
            save_report(filename, csv_lines)
        else:
            save_report(filename, report_lines)


if __name__ == "__main__":
    main()
