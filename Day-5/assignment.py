#1. Write a program that takes a number as input from the user and displays whether the number is even or odd.
num = int(input("enter number: "))
if num % 2 == 0:
    print(num ," is even number")
else:
    print(num ," is odd number")



#2. Write a program that takes a list of numbers as input from the user and displays the sum of all the even numbers in the list.
num = input("enter list of numbers separated by space: ").split()
num = [int(n) for n in num]
a = 0
for n in num:
    if n%2==0:
        a += n
print(a)



#3. Write a program that displays the numbers from 1 to 10 using a for loop. (try with single line)
[print(num ,end=' ') for num in range(1,11)]



#4. Write a program that takes a number as input from the user and displays the multiplication table of the number using a while loop.
num = int(input("\nEnter number: "))
i = 1
while i <= 10:
    ans = num*i
    print(num," * ",i," = ",ans)
    i += 1



#5. Write a program that takes a list of numbers as input from the user and displays only the odd numbers in the list using a for loop.
num = input("enter list of numbers separated by space: ").split()
num = [int(n) for n in num]
odd = []
for n in num:
    if n%2!=0:
        odd.append(n)
print("odd numbers: ",odd)




#6. Write a program that takes a number as input from the user and displays whether the number is prime or not using a try-except block.

try:
    num = int(input("Enter number: "))
    if num <= 1:
        raise ValueError("please enter number greater zero: ")
    for i in range(2,int(num/2)+1):
        if (num%i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is prime number")
except ValueError:
    print("Error")









 

