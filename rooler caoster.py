# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:38:11 2022

@author: BOSS
"""

print("Welcome to RollerCoaster")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride RollerCoaster")
    
    age = int(input("Whats is your Age?"))

    if age < 18:
        bill = 12
        print("In this age you pay $12")
    
    elif age < 12:
        bill = 5
        print("Kids paymentis $5")    
    else :
        bill = 20
        print("Adult payment is $20")
    
    Photos_taking = input("Do you want photos? Y or N.")
    if Photos_taking == "y" :
        bill += 3
        
        print(f"total bill is {bill}")


else:
    print("Wait to grow Taller")
    
      
