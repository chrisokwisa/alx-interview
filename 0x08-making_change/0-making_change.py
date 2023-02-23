#!/usr/bin/python3
""" contains script for file change comes from within"""


def makeChange(coins, total):
    """ determins the fewest number of coins needed """
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed
    # to make up each value from 0 to total
    dp = [float('inf')] * (total+1)
    dp[0] = 0

    # Iterate over the list dp from index 1 to total+1
    for i in range(1, total+1):
        # Iterate over the list of coins
        for coin in coins:
            # Check if the value of the current coin is less than or equal to i
            if coin <= i:
                # Calculate the minimum number of coins
                # needed to make up the remaining value
                subproblem = dp[i-coin] + 1
                # Update dp[i] if the new value is smaller
                dp[i] = min(dp[i], subproblem)

    # Check if a solution was found
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
