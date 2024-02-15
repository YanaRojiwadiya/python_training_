"""List Manipulation:
Write a Python program that takes a list of integers as input and performs the following operations:"""

num = [3,5,2,4,2,3,7,9]

#1. Remove the duplicates from the list.
new_num = list(set(num))
print(new_num)

#2. Sort the list in descending order.
num.sort(reverse=True)
print(num)

#3. Calculate the sum of all the elements in the list.
list_sum = sum(num)
print("sum of all the elements is:",list_sum)


"""Tuple Operations:
Create a tuple containing the names of five countries. Write a Python program that performs the following operations:"""

countries = ("india","USA","japan","peru","china")

#1. Print the length of the tuple.
print(len(countries))

#2. Check if a given country is present in the tuple.
print("USA" in countries)
print("oman" in countries)

#3. Create a new tuple by concatenating the original tuple with another tuple containing five more countries.
new_countries = ("oman","iran","nepal","russia","ukraine")
updated_countries = countries + new_countries
print(updated_countries)

#4. Extra: Try modifying the element at 2nd index. What is output and why. Discuss it.
"""countries[2] = "canada"
print(countries)"""
#it will give a "TypeError:'tuple' object doesn't support item assignment", because tuple is a immutable data type so we cann't modify en elements in tuple.


"""Dictionary Manipulation:
Write a Python program that operates on a dictionary representing the stock of items in a store. The dictionary should contain items as keys and their
corresponding quantities as values. Perform the following operations:"""

stock = {"soap":100,"shampoo":200,"conditioner":200}

#1. Add a new item to the stock.
stock["hair oil"] = 50
print(stock)

#2. Update the quantity of an existing item.
stock["hair oil"] = 40
print(stock)

#3. Remove an item from the stock.
stock.pop("soap")
print(stock)

#4. Print the items in stock alphabetically sorted along with their quantities.
stock_sort = sorted(stock.keys())
for i in stock_sort:
    print(i + ":",stock[i])
#sorting dictionary itself
sorted_stock = {}
for item in sorted(stock):
    sorted_stock[item] = stock[item]
print(sorted_stock)

"""List Comprehensions:
Write a Python program that generates a list of squares of even numbers between 1 and 20 using list comprehension."""

squares = []
for i in range(1,21,2):
    squares.append(i**2) 
print(squares)


"""Dictionary Iteration:
Create a dictionary representing the population of five different cities. Write a Python program that prints the city with the highest population
along with its population."""

population = {"surat":8065000,"ahmedabad":8651000,"delhi":32941000,"mumbai":21297000,"bangalore":13608000}
highest = max(population, key=population.get)
print(highest + ":",population[highest])

#using iterate method
highest_population = 0
highest_city = ""

for city in population:
    if population[city] > highest_population:
        highest_population = population[city]
        highest_city = city
print(highest_city + ":", highest_population)



"""Tuple Unpacking:
Write a Python program that takes a tuple of three integers representing the sides of a triangle as input and determines if it forms a valid triangle.
If it does, print its type (equilateral, isosceles, or scalene)"""

def triangle(sides):
    a, b, c = sorted(sides)

    if a + b > c:
        if a == b == c:
            return "the triangle is equilateral"
        elif a==b or b==c or a==c:
            return "the triangle is isosceles"
        else:
            return "the triangle is scalene"
    else:
        return "not a triangle"

sides=(2,3,4)
print(triangle(sides))
sides=(4,4,4)
print(triangle(sides))
sides=(3,3,5)
print(triangle(sides))
sides=(2,2,5)
print(triangle(sides))


"""List Sorting:
Write a Python program that takes a list of tuples, where each tuple contains a student's name and their score in a test. Sort the list based on the
scores in descending order and print the names of the top three students."""

score = [("yana",89),("yashvi",83),("mishri",85),("polu",87),("chand",80)]
score.sort(key=lambda x: x[1], reverse=True)

for i in range(min(3, len(score))):
    print(score[i][0])


"""Dictionary Filtering:
Create a dictionary representing the prices of different items in a store. Write a Python program that filters out the items with prices less than
a given threshold and prints them."""

prices = {"book":45,"pen":10,"file":25,"colours":250}
threshold = int(input("enter threshold price: "))
print("threshold price: ",threshold)
for i ,price in prices.items():
    if price<threshold:
        print(f"{i}: {price}")
        

"""List Operations:
Write a Python program that takes two lists of integers as input and performs the following operations:"""

list_1 = [1,2,3,4,5,6]
list_2 = [2,4,6,8,10]
print(list_1)
print(list_2)

#1. Find the intersection of the two lists (common elements).
intersection = list(set(list_1)&set(list_2))
print(intersection)
#another method
intersection = []
for x in list_1:
    if x in list_2:
        intersection.append(x)
print(intersection)


#2. Find the union of the two lists (all elements without duplicates).
union = list(set(list_1)|set(list_2))
print(union)
#another method
union = []
for x in list_1:
    if x not in union:
        union.append(x)
for x in list_2:
    if x not in union:
        union.append(x)
print(union)


#3. Find the elements present in the first list but not in the second list.
uniqe_elements_list1 = list(set(list_1)-set(list_2))
print(uniqe_elements_list1)
#another method
uniqe_elements_list1 = []
for x in list_1:
    if x not in list_2:
        uniqe_elements_list1.append(x)
print(uniqe_elements_list1)



"""Dictionary Sorting:
Write a Python program that takes a dictionary containing names as keys and their corresponding ages as values. Sort the dictionary based on ages
in ascending order and print the names of the oldest and youngest person."""

ages = {"parth": 23, "kunj": 24, "nikul": 18}
sort_ages = sorted(ages.items(), key=lambda x: x[1])
print("sorted ages: ",sort_ages)
print("oldest person: ",sort_ages[-1][0])
print("youngest person: ",sort_ages[0][0])







