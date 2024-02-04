# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:16:19 2023

@author: HamzaEren
"""

"""
İlk on doğal sayının kareleri toplamı,

İlk on doğal sayının toplamının karesi,

Dolayısıyla ilk on doğal sayının kareleri toplamı ile toplamın karesi arasındaki fark şu şekildedir:
.

İlk yüz doğal sayının kareleri toplamı ile toplamın karesi arasındaki farkı bulun.
"""


top1 = 0
top2 = 0
for x in range(1,101):
    top1 += x
    top2 += x**2
    
print(top1**2 - top2)
