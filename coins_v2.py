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

def branchOut(i, coins_list):
    print("called branchOut(%i, %s)" % (i, coins_list))
    # This adds O(n)
    coins_sum = sum(coins_list)
    for i in range(i,N):        
        if coins_sum + coins[i] < target:
            # Function is recursive 
            branchOut(i, coins_list + [coins[i]])
        if coins_sum + coins[i] == target:            
            output.append(coins_list + [coins[i]])            
            return
        if coins_sum + coins[i] > target:
            return
    
# Looping at least once, so that is O(n)
for i in range(0,N):
    branchOut(i,[coins[i]])
    
    
# This was damn hard