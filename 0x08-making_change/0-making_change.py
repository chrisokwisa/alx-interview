#!/usr/bin/python3
""" contains script for file change comes from within"""

def makeChange(coins, total):
    """ determins the fewest number of coins needed """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0
    
    # Initialize a list 'dp' of length 'total+1' to store
    # the minimum number of coins needed to reach each amount
    dp = [float('inf')]*(total+1)
    # Set the number of coins needed to reach 0 to 0
    dp[0] = 0
    
    # For each amount from 1 to 'total'
    for i in range(1, total+1):
        # For each coin in 'coins'
        for coin in coins:
            # If the coin is less than or equal to the current amount 'i'
            if coin <= i:
                # Update the minimum number of coins needed 
                # to reach the current amount
                dp[i] = min(dp[i], dp[i-coin]+1)
                
    # If total cannot be met by any number of coins you have, return -1
    # Otherwise, return the minimum number of coins needed to reach 'total'
    return dp[total] if dp[total] != float('inf') else -1
