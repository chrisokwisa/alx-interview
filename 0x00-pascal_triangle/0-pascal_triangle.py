#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    res = []
    row = []
    for i in range(n):
        temp = res[1] + [0]
        row = [1]
        if i > 0:
            for j in range(len(res[-1] + 1):
                row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
