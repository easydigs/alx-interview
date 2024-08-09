#!/usr/bin/python3
"""
n: int The target number of H characters to generate.
Returns: Minimum number of operations needed to get exactly n 'H' characters
"""


def minOperations(n: int) -> int:
    """ Minimum number of operations needed to get exactly n 'H' characters """
    next_segment = 'H'
    body = 'H'
    op = 0

    for i in range(1, n):
        if n % len(body) == 0:
            op += 2  # Copy All + Paste
            next_segment = body
            body += body
        else:
            op += 1  # Paste only
            body += next_segment

        if len(body) == n:
            break

    if len(body) != n:
        return 0

    return op
