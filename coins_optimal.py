# Your quirky boss collects rare, old coins...
# They found out you're a programmer and asked you to solve something they've been wondering for a long time.

# Write a function that, given:

# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.

# Example: for amount=4 (4¢) and denominations=[1,2,3][1,2,3] (1¢, 2¢ and 3¢), your program would output 4—the number of ways to make 4¢ with those denominations:

# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢

coins = [1,2,3]
target = 5
N = len(coins)
output = []


# Consider base cases: No coins given. And, amount = 0

# sol[ x = num of coins. y => target]
solutions = [[0 for x in range(N + 1)] for x in range(0,target + 1)]

 # Fill the enteries for 0 value case (n = 0)
for i in range(N + 1):
    solutions[0][i] = 1
 
for y in range(1, target + 1):
    for x in range(1, N + 1):
        curr_coin = coins[x-1]
        sol_without_coin = solutions[y][x-1]
        if curr_coin <= y:
            sol_with_coin = solutions[y - curr_coin][x]
            solutions[y][x] = sol_with_coin + sol_without_coin
        else:
            solutions[y][x] = sol_without_coin
            
print(solutions[target][N])

# Daamn, this was tough as hell, i dont know how i can make it for my solution