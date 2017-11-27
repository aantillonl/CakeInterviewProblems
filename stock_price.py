# -*- coding: utf-8 -*-

#Suppose we could access yesterday's stock prices as a list, where:
# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
# Write an efficient function that takes stock_prices_yesterday and returns the best
# profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

# For example:
#   stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#   get_max_profit(stock_prices_yesterday)
#   returns 6 (buying for $5 and selling for $11)

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# Initialize index of buying
i_buy = 0

# Initialize max_profit as the first possible move, buy and sell in first and second rounds
# Initialization makes sure it wont be returned with 0 in case no positive profit is encountered
max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[i_buy] 

# Start the for loop from the 2nd element (index 1)
# Since i_buy is the first element (index 0) the profit can only be calculated after the first element
for i in range(1, len(stock_prices_yesterday)):
    profit = stock_prices_yesterday[i] - stock_prices_yesterday[i_buy] 
    # Inline max evaluation and assignation
    max_profit = max(max_profit, profit)
    
    if(stock_prices_yesterday[i] < stock_prices_yesterday [i_buy]):
        i_buy = i

print(max_profit)


# My notes:
# I could brute-force it by just computing all the possible profits and choosing max
# However, the site said it could be done in O(n). Therefore i tried to use indexes to the
# buy and sell prices, in order to calculate the best profit.
# It is possible to keep track of the best profit, and the min price, but when updating the
# min price if a lower is found, then the previous one is lost, and if no better price is found
# i.e. if it is all downhill from there, then the indexes of the actual best buy and sell prices will
# be lost, nevertheless it is exactly as the solution proposed in the website
# It took me a loong while because i wanted to avoid updating the lowest price index if there was no
# certainty that there would also be a highest price after, but it is ok in the end since only the
# absolute profit is required in the output, not the indexes to buy and sell

# Important facts about the prob
#   Can be done in O(n)
#   Can be done in space S(1) (not sure exactly what it means)
#   Does not require to explicitely return the indexes, only the best possible profit
