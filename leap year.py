# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:29:16 2022

@author: BOSS
"""


year = int(input("Which year do you want to check?"))


if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
          print("leap year")
      else:
        print("Not leap year")
    else:
        print("leap year")
else: 
        print("Not leap year")
    
        