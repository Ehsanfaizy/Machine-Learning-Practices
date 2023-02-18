#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      BOSS
#
# Created:     28/12/2022
# Copyright:   (c) BOSS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

for number in range(1,101):
   if number % 3==0 and 5 == 0:
    print("FizzBuzz")
   elif number % 3 == 0:
        print("Fizz")
   elif number % 5 == 0:
        print("Buzz")
   else:
     print(number)
