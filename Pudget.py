#version 1.1

#List of bills in values
Bills=[650,30,60,20,65,97]

def add(Bills):
    Total=0
    for i in Bills:
        Total+=i
        return Total

#Amount of income 
Income=900

#Some other examples of income:
#Income2=500 
#TaxReturn=1400


result=add(Bills)

print("Total Income:", Income )
print("Total amount of bills per month:", result)
print("Total amount needed to save each check:", result /2)
print("Leftover each check:", Income - result /2)
