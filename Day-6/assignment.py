"""1. Write a program that defines a function to calculate the area of a rectangle. The function should take the length and width of the rectangle as input
parameters and return the area."""
def area_of_rectangle(length,width):
    area = length * width
    return area

A = area_of_rectangle(3,5)
print(A)

"""2. Write a program that defines a function to calculate the factorial of a number. The function should take a single input parameter and return the
factorial of that number."""

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num = num*i
    return num

a = factorial(7)
print(a)

"""3. Write a program that defines a function to calculate the sum of a list of numbers. The function should take a list of numbers as input and return the
sum of those numbers."""

def sum_of_list(num):
    n = 0
    for i in num:
        n +=i
    return n

num = [1,2,3,4]
a = sum_of_list(num)
print(a)

"""4. Write a program that defines a function to calculate the nth Fibonacci number. The function should take a single input parameter and return the nth
Fibonacci number."""

def fibonacci_number(num):
    a=0
    b=1
    for i in range(1,num+1):
        c = a + b
        a = b
        b = c
    return c

num = 5
a = fibonacci_number(num)
print(a)


"""5. Create a module called my_module that defines a function to calculate the square of a number. Import the module into a new program and use the function
to calculate the square of a number."""

from my_module import square

n = int(input("enter a number: "))
num = square(n)
print(num)







