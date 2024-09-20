#!/usr/bin/python3
"""
Generate changes needed to reach total

Args:
    coins ([List]): [List of Coins available]
    total ([int]): [total amount needed]
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    check = 0
    temp = 0
    coins.sort(reverse=True)

    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1

    return -1
