#version 1.0

#List of bills here
Bills=[650,30,60,20,65,97]

def add(Bills):
    Total=0
    for i in Bills:
        Total+=i
        return Total

#Amount of Paycheck goes here
paycheck=900

result=add(Bills)

print("Pacheck:", paycheck)
print("Total amount of bills per month:", result)
print("Total amount needed to save each check:", result /2)
print("Leftover each check:", result /2 - paycheck)
