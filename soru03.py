# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:03:13 2023

@author: HamzaEren
"""

"""
3) The prime factors of 13195 are 5, 7, 13 and 29.
   What is the largest prime factor of the number 600851475143?

3) 13195'in asal çarpanları 5, 7, 13 ve 29'dur.
   600851475143 sayısının en büyük asal çarpanı nedir?
"""


def isPrime(n):
    for x in range(2, int(n/2)):
        if n % x == 0:
            return False
    return True

def question3(number):
    if isPrime(number):
        return number
    for x in range(int(number/2), 2, -1):
        if number % x == 0 and isPrime(x):
            return x

number = 1319553531
print(question3(number))
