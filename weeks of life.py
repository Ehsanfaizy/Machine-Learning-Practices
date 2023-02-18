# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:30:53 2022

@author: BOSS
"""

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remainig = years_remaining *365
weeks_remaining = years_remaining * 52
months_remainig = years_remaining * 12

message = f"you have {days_remainig} days, {weeks_remaining} weeks, and{months_remainig} months left."
print(message)

#Write your code below this line 👇
