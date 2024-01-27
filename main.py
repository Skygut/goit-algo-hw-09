def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    change = {}

    for coin in coins:
        if amount >= coin:
            coin_count = amount // coin
            amount -= coin_count * coin
            change[coin] = coin_count

            if amount == 0:
                break

    return change


def find_min_coins(total, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float("inf")] * (total + 1)
    min_coins[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    result = {}
    current_total = total
    while current_total > 0:
        for coin in sorted(coins):
            if min_coins[current_total - coin] == min_coins[current_total] - 1:
                result[coin] = result.get(coin, 0) + 1
                current_total -= coin
                break

    return result


print(find_coins_greedy(113))
print(find_min_coins(113))
