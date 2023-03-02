#!/usr/bin/python3
""" Should be an executable file """


def island_perimeter(grid):
    # Variables to keep track of perimeter and dimensions of grid
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Loop through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # If the cell is land, check its neighbors
            if grid[row][col] == 1:
                # Check north neighbor
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check south neighbor
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check west neighbor
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check east neighbor
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    # To handle the case of multiple islands,
    # we will count the number of islands
    # and the perimeter of the outermost layer.
    island_count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                island_count += 1
                # Flood-fill the island with a unique number
                # so we can count its size.
                dfs(grid, row, col, island_count + 1)
                break
        if island_count > 0:
            break

    # Find the outermost layer of the island (marked with island_count + 1)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == island_count + 1:
                # Check north neighbor
                if row == 0 or grid[row - 1][col] != island_count + 1:
                    perimeter += 1
                # Check south neighbor
                if row == rows - 1 or grid[row + 1][col] != island_count + 1:
                    perimeter += 1
                # Check west neighbor
                if col == 0 or grid[row][col - 1] != island_count + 1:
                    perimeter += 1
                # Check east neighbor
                if col == cols - 1 or grid[row][col + 1] != island_count + 1:
                    perimeter += 1

    # Return the total perimeter
    return perimeter


# Helper function for flood-filling an island with a unique number.
def dfs(grid, row, col, number):
    # Base case: if cell is not land, stop.
    if not (0 <= row < len(grid)
            and 0 <= col < len(grid[0])) or grid[row][col] != 1:
        return
    # Mark cell as visited with the given number.
    grid[row][col] = number
    # Recursively fill its neighbors with the same number.
    dfs(grid, row - 1, col, number)
    dfs(grid, row + 1, col, number)
    dfs(grid, row, col - 1, number)
    dfs(grid, row, col + 1, number)
