#!/usr/bin/python3
""" Contains the code that determines if each box contains keys to the other boxes
"""


def canUnlockAll(boxes):
    """ This method determines if all the boxes can opened """
    # set  of the visited boxes
    visited = set()

    # Recusrsive helper function to explore all reachablr boxes
    def dfs(i):
        # Mark the current box as visited
        visited.add(i)

        # Explore each box that cn be reached from the current box
        for j in boxes[i]:
            if j not in visited:
                dfs(j)

    # start the depth-first search to explore all the boxes that can be reached from the first box, False otherwise
    dfs(0)
    
    return len(visited) == len(boxes)


# This function works by using a depth-first search to explore all the boxes that can be reached from the first box (which is unlocked).
# If the depth-first search visits all the boxes, it means that all the boxes can be opened and the function returns True.
# Otherwise, the function returns False.


# The time complexity of the canUnlockAll function is O(n), where n is the number of boxes.
# This is because the function performs a depth-first search, which involves visiting each box at most once.

# The space complexity of the function is also O(n), as the function stores the visited boxes in a set, which takes O(n) space.

# Note that this is assuming that each box contains at most a constant number of keys. If the number of keys in each box is not constant,
# the time and space complexity of the function would be dependent on the number of keys as well.
