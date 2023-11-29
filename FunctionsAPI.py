from flask import abort

#Fibonacci 
def fib(x):

    data = [1, 1]

    for i in range(x-2):
        data[0], data[1] = data[1], data[0]+data[1]

    return data[1]

#Factorial 
def fact(x) -> int:

    value = 1

    for i in range(1,x+1):
        value *= i
    
    return value

#Error handling
def errorAnalise(data):

    if len(data) > 2:
        return abort(400, description='Json too long')

    for value in data.values():
        if type(value) != int:
            return abort(400, description='Invalid type for value')