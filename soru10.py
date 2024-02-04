# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:41:27 2023

@author: HamzaEren
"""

def isPrime(number):
    if number == 1:
        return False
    for x in range(2, int(number/2)):
        if number % x == 0:
            return False
    return True

toplam = 0
for x in range(2, 2000000):
    if isPrime(x):
        toplam += x
        
print(toplam)