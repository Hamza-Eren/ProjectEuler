# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:28:59 2023

@author: HamzaEren
"""

for x in range(1, 1000):
    for y in range(x+1, 1000):
        for z in range(y+1, 1000):
            if x**2 + y**2 == z**2 and x + y + z == 1000:
                print(f"x: {x} | y: {y} | z: {z}")
            
