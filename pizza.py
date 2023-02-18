# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:06:17 2022

@author: BOSS
"""

print("Welcome to Python Pizza delivery!")

size = input("what size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you Want to Pepperoni? Y or N")
extra_chees = input("Do want extra cheees? Y or N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
     bill += 20
else:
     bill += 25

if add_pepperoni == "Y":
   if size == "S":
        bill += 2
   else:
       bill += 3
         
if extra_chees == "Y":
         bill += 1
         
print(f"Your final bill is ${bill}")
         
         
         
        
     