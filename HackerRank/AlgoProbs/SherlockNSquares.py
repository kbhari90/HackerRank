'''
Created on 31-Jan-2015

@author: bharath_kalyans
#################
Problem Statement
#################

Watson gives two integers A & B to Sherlock and asks if he can count the number of square integers between A and B (both inclusive).

A square integer is an integer which is the square of any integer. For example, 1, 4, 9, 16 are some of the square integers as they are squares of 1, 2, 3, 4 respectively.

Input Format 
First line contains T, the number of testcases. T test cases follow, each in a newline. 
Each testcase contains two space separated integers denoting A and B.

Output Format 
For each testcase, print the required answer in a new line.

Constraints 
1 <= T <= 100 
1 <= A <= B <= 109

Sample Input

2
3 9
17 24
Sample output

2
0
Explanation 
Test Case #00: In range [3,9], 4 and 9 are the two square numbers. 
Test Case #01: In range [17,24], there are no square numbers.


'''
import math

def checkSquareNumbers(noOfInputs):
    for i in range(noOfInputs):
        
        x=[int(z) for z in input().split(' ')]
        print(int(math.floor(math.sqrt(x[1])))-math.ceil(math.sqrt(x[0]))+1)

if __name__=='__main__':
    print("Enter the number of inputs:")
    noOfInputs=int(input())
    print("Enter the numbers for checking:")
    checkSquareNumbers(noOfInputs) 
