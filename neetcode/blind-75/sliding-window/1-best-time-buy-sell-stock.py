# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


# input: list of prices for for a stock on idx day
# output: max profit you can achieve

# create buy and have it point to idx 0
# create sell and have it point to idx 1
# create max_profit and initialize to 0
# while loop to iterate while sell is less then len(prices)
# create profit and have it equal prices[sell] - prices[buy]
# if profit > max_profit reassign max and increment sell
# else increment buy and sell
# return max_profit

def maxProfit(prices):
    buy = 0
    sell = 1
    max_profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
        else:
            buy = sell
        sell += 1

    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
# Output: 5
