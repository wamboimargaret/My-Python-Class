# Question 1
# Write a function that uses while, if and continue statements 
# to print all the even numbers between 0 and 50.
def even_numbers():
    num = 0
    while num <= 50:
        if num % 2 != 0:
            num += 1
            continue
        print(num)
        num += 1

# Question 2
# Write a function that takes an integer argument and prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.
def prime_number(n):
    if n < 2:
        print("Not prime")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")

# Question 3
# Write a function that takes a list of integers as input and prints the 
# sum of all the even numbers in the list.
def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    print(total)


# Question 4
# Write a function that takes any two integers as input, and prints the sum of all the numbers 
# between the two integers (inclusive) that are divisible by 3.
def sum_of_integers_divisible_by_three(a, b):
    empty_list_of_numbers = []
    for i in range(a, b+1 ):
        if i % 3 == 0:
            empty_list_of_numbers.append(i)
    return empty_list_of_numbers