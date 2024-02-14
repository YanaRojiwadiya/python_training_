"""Problem 1
Problem Description: Print a Pattern According to The Given Value of A.
Example: For A = 3 pattern looks like:
1 0 0
1 2 0
1 2 3

Problem Constraints
1 <= A <= 1000

Input Format
The first and only argument is an integer denoting A.

Example Input
Input 1:
 A = 3

Input 2:
 A = 4
 
Output Format
Return a two-dimensional array where each row in the returned array represents a row in the pattern.

Example Output
Output :1
 [
   [1, 0, 0]
   [1, 2, 0]
   [1, 2, 3]
 ]

Output 2:
 [
   [1, 0, 0, 0]
   [1, 2, 0, 0]
   [1, 2, 3, 0]
   [1, 2, 3, 4]
 ]


Example Explanation
Explanation 2:

 For A = 4 pattern looks like:  

                             1 0 0 0
                             1 2 0 0
                             1 2 3 0
                             1 2 3 4

 So we will return it as a two-dimensional array."""


n = int(input("enter integer n:"))

for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            print(j, end=" ")
        else:
            print(0, end=" ")
    print()





"""Problem 2:
Problem Description:
You are given an array of integers A of size N.

Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.


Problem Constraints

2 <= N <= 1e5

-1e9 <= A[i] <= 1e9

There is atleast 1 odd and 1 even number in A


Input Format
The first argument given is the integer array, A.


Output Format
Return maximum among all even numbers of A - minimum among all odd numbers in A.


Example Input

Input 1:
 A = [0, 2, 9]

Input 2:
 A = [5, 17, 100, 1]


Example Output
Output 1:
-7

Output 2:
99



Example Explanation

Explanation 1:
Maximum of all even numbers = 2
Minimum of all odd numbers = 9
ans = 2 - 9 = -7

Explanation 2:
Maximum of all even numbers = 100
Minimum of all odd numbers = 1
ans = 100 - 1 = 99"""

A = [5, 17, 100, 1]
even = []
odd = []
for i in A:
    if i%2==0:
        even.append(i)
    if i%2!=0:
        odd.append(i)

diff = max(even) - min(odd)
print(diff)






"""Problem 3:
Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? Hint: X-OR


Problem Constraints

1 <= |A| <= 2000000

0 <= A[i] <= INTMAX


Input Format
The first and only argument of input contains an integer array A.


Output Format
Return a single integer denoting the single element.

Example Input

Input 1:
 A = [1, 2, 2, 3, 1]

Input 2:
 A = [1, 2, 2]


Example Output

Output 1:
 3

Output 2:
 1


Example Explanation

Explanation 1:

3 occurs once.

Explanation 2:

1 occurs once."""

A = [1, 2, 2, 3, 1]

num = 0
for i in A:
    num = num^i
print(num)
    




"""Problem 4: Q4. Time to equality

Problem Description
Given an integer array A of size N. In one second, you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.

Problem Constraints

1 <= N <= 1000000

1 <= A[i] <= 1000


Input Format
First argument is an integer array A.


Output Format
Return an integer denoting the minimum time to make all elements equal.


Example Input
A = [2, 4, 1, 3, 2]


Example Output
8

Example Explanation
We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds."""

A = [2, 4, 1, 3, 2]
maximun = max(A)
count = 0
for i in A:
    count += maximun - i
print("The time required will be ",count," seconds")










