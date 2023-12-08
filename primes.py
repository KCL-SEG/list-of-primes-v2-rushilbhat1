"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def isPrime(num):
    for i in range (2, math.floor(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError("Invalid input")
    
    num=2
    while len(list) < number_of_primes:
        if (isPrime(num)):
            list.append(num)
        num += 1

    return list
