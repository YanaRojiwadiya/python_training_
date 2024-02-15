
"""1. Write a program that takes two numbers as input from the user and displays their sum."""
A = int(input("enter value of A: "))
B = int(input("enter value of B: "))
print("sum of A and B is: " ,A+B)

"""2. Write a program that takes a string as input from the user and displays it in uppercase letters."""
string = input("enter your name: ")
print(string.upper())

"""3. Write a program that displays the following text, using triple quotes:
Programming is fun. 
I love Python."""
print("""Programming is fun. 
I love Python.""")

"""4. Write a program that displays the following text, using escape characters:
She said, "Hello, world!" """
print("She said, \"Hello, world!\"")
print('She said, "Hello, world!"')

"""5. Write a program that takes a sentence as input from the user and displays the number of words in the sentence."""  
sentence = input("enter any sentence: ")
s = sentence.split()
words = len(s)
print("words in sentence: ",words)
