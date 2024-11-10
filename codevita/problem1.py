def calculate_profit_loss(stock_data, prices, current_time):
    
    realized_profit = 0
    unrealized_profit = 0

    for quantity, buy_time, sell_time in stock_data:
        if sell_time == 0:
            # Stock not sold - Unrealized P/L
            current_price = prices[current_time - buy_time]
            unrealized_profit += (current_price -
                                  prices[buy_time - 1]) * quantity
        else:
            # Stock sold - Realized P/L
            sell_price = prices[sell_time - 1]
            buy_price = prices[buy_time - 1]
            realized_profit += (sell_price - buy_price) * quantity

    return realized_profit, unrealized_profit


# Read input
num_stocks = int(input())
stock_data = []
for _ in range(num_stocks):
    quantity, buy_time, sell_time = map(int, input().split())
    stock_data.append((quantity, buy_time, sell_time))

num_prices = int(input())
prices = list(map(int, input().split()))

current_time = int(input())

# Calculate realized and unrealized P/L
realized_profit, unrealized_profit = calculate_profit_loss(
    stock_data, prices, current_time)

# Print output
print(realized_profit)
print(unrealized_profit)
