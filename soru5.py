# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:18:23 2023

@author: HamzaEren
"""

sayi = 1
for x in range(19, 1, -1):
    if sayi % x == 0:
        continue
    sayi *= x
    
print(sayi)