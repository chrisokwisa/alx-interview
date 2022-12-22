#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    res = []
    row = []
    for i in range(n):
        # temp = res[1] + [0]
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(res[-1][j:j+2]))
        res.append(row)
    return res
