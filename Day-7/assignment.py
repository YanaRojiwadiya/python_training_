#1. Write a program that opens a text file and reads the contents of the file.
file = open('example.txt','r')

for i in file:
    print(i)

#2. Write a program that opens a text file and writes some text to the file.
file = open('example.txt','w')

file.write('This is a sample text.')
file.close()


#3. Write a program that opens a binary file and reads the first 10 bytes of the file.
file = open('example.txt', 'r')
data = file.read(10)
print(data) 


#4. Write a program that creates a new text file, writes some text to the file, and then renames the file.
import os


#5. Write a program that deletes a text file.
os.remove('example.txt')
 
