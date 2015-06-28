# Enter your code here. Read input from STDIN. Print output to STDOUT
n, _ = [int(x) for x in raw_input().split()]
coins = sorted([int(x) for x in raw_input().split()])

def coinChange(n, coins):
    coin_collection_counts = [1] + [0] * n # there is only one way to reach value zero
    for coin in coins:
        for value in xrange(len(coin_collection_counts)):
            if coin + value <= n:
                coin_collection_counts[value + coin] += coin_collection_counts[value]
            else:
                break
    return coin_collection_counts[n]

print coinChange(n, coins)
