#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BOSS
#
# Created:     30/12/2022
# Copyright:   (c) BOSS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
emp1 = employee("ehsan", 23, 100000)
emp2 = employee("Faizy",23,200000)
print(emp1.__dict__)
print(emp2.__dict__)
