# CodeAlpha Task 2 - Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 280,
    "MSFT": 330,
    "AMZN": 200
}

portfolio = {}

print("\n==============================")
print("   STOCK PORTFOLIO TRACKER")
print("==============================")

while True:
    stock_name = input("\nEnter stock symbol (AAPL/TSLA/GOOG/MSFT/AMZN): ").upper().strip()

    if stock_name not in stock_prices:
        print(">> Stock symbol not recognized. Please try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity < 0:
            print(">> Quantity cannot be negative.")
            continue
    except ValueError:
        print(">> Invalid input. Please enter a whole number.")
        continue

    portfolio[stock_name] = quantity

    more = input("Do you want to add another stock? (y/n): ").lower().strip()
    if more not in ["y", "yes"]:
        break
print("\n===== PORTFOLIO SUMMARY =====")
total_value = 0  

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment
    print(f"{stock} - {quantity} shares x ${price} = ${investment}")

print(f"\nTotal Portfolio Value = ${total_value}")

#Saving summary to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=========================\n")
    
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} - {quantity} shares x ${price} = ${investment}\n")
    file.write(f"\nTotal Portfolio Value = ${total_value}")

print("\n>> Summary file generated successfully: portfolio_summary.txt")