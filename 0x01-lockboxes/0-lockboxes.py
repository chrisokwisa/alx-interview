#!/usr/bin/python3
""" determines if each box contains keys to the other boxes"""


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

    # start the depth-first
    dfs(0)

    return len(visited) == len(boxes)
