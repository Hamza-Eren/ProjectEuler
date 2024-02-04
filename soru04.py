# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:21:41 2023

@author: HamzaEren
"""

def isPol(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

max_number = 0
x_n = 0
y_n = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        if isPol(x*y) and x*y > max_number:
            max_number = x*y
            x_n, y_n = x, y
            
print(f"{x_n} x {y_n} = {max_number}")
