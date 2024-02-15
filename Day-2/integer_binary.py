"""Create function in python which take integer as input and convert it to binary string
Input 5 → 101, 7 → 111"""

def integer_to_binary(number):
    binary = ""  
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

number = int(input("Enter integer value: "))
binary_value = integer_to_binary(number)
print(binary_value, "is a binary value of", number)
