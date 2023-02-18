# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:13:11 2022

@author: BOSS
"""

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
bmi = round(weight / height **2)
print(bmi)
#Write your code below this line 👇 
if bmi < 18.5:
  print("u r Underweight")
elif bmi < 25 :
  print("Normal weight")
elif bmi < 30 :
  print("u r Over weight")
elif bmi < 35:
  print("Obese")
else:
  print("Go to Docter")



