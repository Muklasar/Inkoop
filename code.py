icity = input("enter your city ").capitalize()
icor = input("cost or rating ")
iopration = input("opretion ")

import json

with open('data.json') as f:
    data = json.load(f)

def match(icity, icor, iopration, data):
    mcity = [dt for dt in data if dt["city"] == icity]
    cost = [ct["cost"] for ct in mcity]
    rating = [ct["rating"] for ct in mcity]
    if mcity and icor=="cost":
        return f'{iopration} cost of Hotel in {icity} is Rs.{minmax(cost, iopration)}.'
    elif mcity and icor=="rating":
        return f'{iopration} rating of Hotel in {icity} is {minmax(rating, iopration)} Stars.'
    else:
        print("invalid")

def minmax(value, iopration):
    if iopration == "highest":
        return highest(value)
    elif iopration == "lowest":
        return lowest(value)
    elif iopration == "average":
        average = sum([int(i) for i in value]) // len(value)
        return average
    else:
        print("invalid")

def highest(value):
    myMax = value[0]
    for num in value:
        if num > myMax:
            myMax = num 
    return myMax

def lowest(value):
    myMax = value[0]
    for num in value:
        if num < myMax:
            myMax = num 
    return myMax

result = match(icity, icor, iopration, data)
print(result)

       

