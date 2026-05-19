def max_profit(prices):
    if len(prices) < 2:
        return "Not enough days"

    min_price = prices[0]
    min_day = 0

    best_profit = 0
    buy_day = -1
    sell_day = -1

    for i in range(1, len(prices)):
        profit = prices[i] - min_price

        if profit > best_profit:
            best_profit = profit
            buy_day = min_day
            sell_day = i

        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i

    if best_profit <= 0:
        return "No profitable transaction possible"

    return {
        "buy_day": buy_day + 1,
        "sell_day": sell_day + 1,
        "profit_per_share": best_profit,
        "total_profit_for_1000_shares": best_profit * 1000
    }


prices = [9, 1, 5]

print(max_profit(prices))
