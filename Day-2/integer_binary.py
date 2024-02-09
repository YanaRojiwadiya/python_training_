"""Create function in python which take integer as input and convert it to binary string
Input 5 → 101, 7 → 111"""

def integer_to_binary(number):
    return bin(number)[2:]
number = int(input("enter int value:"))
print(integer_to_binary(number),"is a binary value of ", number)
