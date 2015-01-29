'''
Created on Jan 29, 2015

@author: bharath_kalyans

Problem Statement

Given a list of N integers, your task is to select K integers from the list such that it's unfairness is minimized.

if (x1,x2,x3,…,xk) are K numbers selected from the list N, the unfairness is defined as

max(x1,x2,…,xk) - min(x1,x2,…,xk)
where max denotes the largest integer among the elements of K, and min denotes the smallest integer among the elements of K.

Input Format 
The first line contains an integer N. 
The second line contains an integer K. N lines follow. Each line contains an integer that belongs to the list N.

Note

Integers in the list N may not be unique.

Output Format 
An integer that denotes the minimum possible value of unfairness.

Constraints 
2<=N<=105 
2<=K<=N 
0<=integer in N <=109
Sample Input #00

7
3
10
100
300
200
1000
20
30
Sample Output #00

20
Explanation #00 
Here K=3, selecting the 3 integers such that K = 10,20,30 candies. The unfairness is

max(10,20,30) - min(10,20,30) = 30 - 10 = 20
'''
print("Enter the number of entries")
n = int(input())
print("Enter the Number of selections")

k = int(input())
print("Enter the numbers:")
givenList = []
for i in range(n):
    givenList.append(int(input()))
    
def calculateUnfairness(givenList):
    diff = 999999999
    givenList.sort()
    #Here the logic is that we are selecting the numbers k from the list givenList,
    # and comparing between the maximum of the selection k(from sorted list) with the minimum of 
    #selection k from the same list. Hence the loop should only fo till the the whole length-selection +1(for python range function which takes only till the last to before value in loop) 
    for i in range(n-k+1):
        #Here the last value of the selection(i+k-1)  is subtracted from the first value of the selction(i)
        temp  = givenList[i+k-1] - givenList[i]
        if temp<diff:
            #smallest difference is recorded in diff
            diff = temp
    return diff 

print(calculateUnfairness(givenList))