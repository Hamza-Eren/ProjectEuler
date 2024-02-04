# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:49:12 2023

@author: HamzaEren
"""

"""
1) If we list all the natural numbers below 10 that are multiples of 3 or 5,
   we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all
   the multiples of 3 or 5 below 1000.

1) 10'un altındaki 3 veya 5'in katı olan tüm doğal sayıları sıralarsak
   3, 5, 6 ve 9 elde ederiz. Bu katların toplamı 23'tür. 3 veya 5'in 1000'in
   altındaki tüm katlarının toplamını bulun.
"""

toplam = 0
for x in range(1000):
    if (x % 3 == 0) or (x % 5 == 0):
        toplam += x
        
print(toplam)
