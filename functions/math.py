def add (a, b):
    answer = a + b 
    return answer

def subtract(c, d):
    answer1 = c - d
    return answer1

def multiply(e, f):
    answer2 = e * f
    return answer2

def divide(g, h):
    answer3 = g / h
    return answer3

def remainder(i, j):
    answer4 = i % j
    return answer4

def sum(*numbers):
    answer = 0
    for number in numbers:
        answer+=number
    return answer

def multiplication(*nums):
    mul = 1
    for num in nums:
        mul*=num
    return mul

def sum(*numbers):
    answer = 0
    for number in numbers:
        answer+=number
    return answer