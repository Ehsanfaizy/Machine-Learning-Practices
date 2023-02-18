# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 23:04:38 2022

@author: BOSS
"""

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

number_items = len(names)

random_choice = random.randint(0, number_items -1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + "is going to pay the bill")

