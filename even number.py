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

total = 0

for number in range(1,101):
   if number % 2 == 0:
    total += number
print(total)

