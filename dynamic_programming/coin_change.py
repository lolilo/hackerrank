# Enter your code here. Read input from STDIN. Print output to STDOUT
n, _ = [int(i) for i in raw_input().split()]
coins = sorted([int(i) for i in raw_input().split()])

def coinChange(n, coins):
    # table index represents target value
    # values are arrays of coin arrays; each coin array shows a collectino of coins that add up to target value
    table = [[] for x in xrange(n + 1)]
    table[0] = [[]] # it takes zero coins to make value zero

    for target_value in xrange(1, n+1): # populate table
        for coin in coins:
            if coin > target_value:
                continue
            if len(table[target_value - coin]) > 0:
                for coin_array in table[target_value - coin]:
                    new_coin_array = sorted(coin_array[:] + [coin])
                    if new_coin_array not in table[target_value]:
                        table[target_value].append(new_coin_array)

    # print table
    return table[n]


# n = 4
# coins = [1, 3, 4]
print len(coinChange(n, coins))
