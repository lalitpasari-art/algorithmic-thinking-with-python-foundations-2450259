import functools as ft

denominations = [200, 100, 50, 20, 10, 5, 2, 1]

@ft.lru_cache(maxsize=None)
def make_change(target_amount):
    if target_amount in denominations or target_amount == 0:
        return 1
    min_coins = float('inf')
    for coin in denominations:
        if coin <= target_amount:
            num_coins = 1 + make_change(target_amount - coin)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p
print(make_change(200))  # 5: £1 + 50p + 10p + 2p + 1p
print(make_change(263))  # 5: £2 + 50p + 10p + 2p + 1p