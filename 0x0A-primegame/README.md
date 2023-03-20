# Maria and Ben's Game
Maria and Ben are playing a game where they take turns choosing a prime number and removing that number and its multiples from a set of consecutive integers starting from 1 up to and including `n`. The player who cannot make a move loses the game. They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

# Prototype

``` 
def isWinner(x: int, nums: List[int]) -> Union[str, None]:
    
pass
```

# Input
*  `x`: an integer, the number of rounds to play (1 <= x <= 10000)
* `nums`: a list of integers, each denoting n for each round (1 <= n <= 10000)

# Output
* Returns a string with the name of the player who won the most rounds.
* If the winner cannot be determined, returns None.

```
x = 3
nums = [4, 5, 1]

# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers left for Maria to choose

assert isWinner(x, nums) == 'Maria'

```  

* N/B
Ben has the most wins