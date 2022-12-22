#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    res = [[1]]
    for i in range(n - 1):
        temp = [0] + [res-1] + [0]
        row = []
        for j in range(len[res-1] + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
