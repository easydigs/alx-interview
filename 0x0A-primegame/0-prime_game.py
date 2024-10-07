#!/usr/bin/python3
"""Module for Prime Game."""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of integers where each integer n denotes
                            a set of consecutive integers starting from 1
                            up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
             or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Check for invalid input
    if x <= 0 or nums is None or x != len(nums):
        return None

    # Initialize scores
    ben = 0
    maria = 0

    # Create a list 'primes' of length max(nums) + 1, all elements initialized
    # to 1. Set the first two elements, primes[0] and primes[1], to 0 because
    # 0 and 1 are not prime numbers.
    max_num = max(nums)
    primes = [1] * (max_num + 1)
    primes[0], primes[1] = 0, 0

    # Use the Sieve of Eratosthenes to mark prime numbers in the list
    for i in range(2, len(primes)):
        rm_multiples(primes, i)

    # Play each round of the game
    for n in nums:
        # If the sum of prime numbers in the set is even, Ben wins the round
        if sum(primes[0:n + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, prime):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        ls (list of int): An array of possible prime numbers.
        prime (int): The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    # Mark multiples of the prime as non-prime by setting their value to 0
    for i in range(2, len(ls)):
        if i * prime < len(ls):
            ls[i * prime] = 0
        else:
            break
