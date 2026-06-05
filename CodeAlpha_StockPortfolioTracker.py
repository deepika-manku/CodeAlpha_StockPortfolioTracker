# CodeAlpha Task 2 - Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 280,
    "MSFT": 330,
    "AMZN": 200
}

portfolio = {}
total_value = 0

print("\n==============================")
print("   STOCK PORTFOLIO TRACKER")
print("==============================")

while True:
    stock_name = input("\nEnter stock symbol (AAPL/TSLA/GOOG/MSFT/AMZN): ").upper()

    if stock_name not in stock_prices:
        print("Stock not available in tracker.")
        continue

    quantity = int(input(f"Enter quantity of {stock_name}: "))

    portfolio[stock_name] = quantity

    more = input("Do you want to add another stock? (yes/no): ").lower()
    if more != "yes":
        break


print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment

    print(f"{stock} - {quantity} shares × ${price} = ${investment}")


print(f"\nTotal Portfolio Value = ${total_value}")


# Saving to file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=========================\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(
            f"{stock} - {quantity} shares x ${price} = ${investment}\n"
        )

    file.write(f"\nTotal Portfolio Value = ${total_value}")

print("\nPortfolio saved successfully in portfolio_summary.txt")