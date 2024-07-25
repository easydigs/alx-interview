#!/usr/bin/python3
"""
n (int): The number of rows in Pascal's triangle.
Return: A list of integers representing the Pascal Triangle
        of n returns empty list if n <= 0
"""

def pascal_triangle(n):

    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k
