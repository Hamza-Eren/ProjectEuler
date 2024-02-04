# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:21:23 2023

@author: HamzaEren
"""

def isPrime(number):
    if number == 1:
        return False
    for x in range(2, int(number/2)):
        if number % x == 0:
            return False
    return True

number = 0
i = 0
x = 1
while i <= 1001:
    if isPrime(x):
        number = x
        x += 1
        i += 1
    else:
        x += 1
        
        
print(number)