"""Problem 1: Array with consecutive elements
Problem Description

Given an array of positive integers A, check and return whether the array elements are consecutive or not.

NOTE: Try this with O(1) extra space.


Problem Constraints

1 <= length of the array <= 105

1 <= A[i] <= 109


Input Format

The only argument given is the integer array A.


Output Format

Return 1 if the array elements are consecutive else return 0.


Example Input

Input 1:

 A = [3, 2, 6, 4, 5]

Input 2:

 A = [1, 3, 2, 5]


Example Output

Output 1:

 1

Output 2:

 0


Example Explanation

Explanation 1:

 As you can see all the elements are consecutive (i.e 2, 3, 4, 5, 6), so we return 1.

Explanation 2:

 Element 4 is missing, so we return 0."""

A = [1, 3, 4, 2, 5]
A.sort()
print(A)
B = ()
for i in range(len(A)-1):
    if A[i]+1==A[i+1]:
        B = 1
    else:
        B = 0
        break
print(B)











"""Problem 2: Colorful Number

Given a number A, find if it is COLORFUL number or not.

If number A is a COLORFUL number return 1 else, return 0.


What is a COLORFUL Number:

A number can be broken into different consecutive sequence of digits.

The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245.


This number is a COLORFUL number, since the product of every consecutive sequence of digits is different


Problem Constraints

1 <= A <= 2 * 109



Input Format

The first and only argument is an integer A.


Output Format

Return 1 if integer A is COLORFUL else return 0.


Example Input

Input 1:

 A = 23

Input 2:

 A = 236


Example Output

Output 1:

 1

Output 2:

 0



Example Explanation

Explanation 1:


 Possible Sub-sequences: [2, 3, 23] where

 2 -> 2

 3 -> 3

 23 -> 6 (product of digits)

 This number is a COLORFUL number since product of every digit of a sub-sequence are different.

Explanation 2:


 Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where

 2 -> 2

 3 -> 3

 6 -> 6

 23 -> 6 (product of digits)

 36 -> 18 (product of digits)

 236 -> 36 (product of digits)

 This number is not a COLORFUL number since the product sequence 23 and sequence 6 is same"""


A = 234














