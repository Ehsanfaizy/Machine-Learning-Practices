# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 00:01:15 2022

@author: BOSS
"""

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

who_will_pay = random.choice(names)
print(who_will_pay + "is going to pay the bill")