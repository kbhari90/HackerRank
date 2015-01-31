'''
Created on Jan 30, 2015

@author: bharath_kalyans

#################
Problem Statement
#################

Animesh has N empty candy jars, numbered from 1 to N, with infinite capacity. He performs M operations. Each operation is described by 3 integers a, b and k. Here, a and b are indices of the jars, and k is the number of candies to be added inside each jar whose index lies between a and b (both inclusive). Can you tell the average number of candies after M operations?

Input Format 
The first line contains two integers N and M separated by a single space. 
M lines follow. Each of the M lines contain three integers a, b and k separated by single space.

Output Format 
A single line containing the average number of candies across N jars, rounded down to the nearest integer.

Note 
Rounded down means finding the greatest integer which is less than or equal to given number. Eg, 13.65 and 13.23 are rounded down to 13, while 12.98 is rounded down to 12.

Constraints 
3 <= N <= 107 
1 <= M <= 105 
1 <= a <= b <= N 
0 <= k <= 106

Sample Input #00

5 3
1 2 100
2 5 100
3 4 100
Sample Output #00

160
Explanation 
Initially each of the jar contains 0 candies

0 0 0 0 0  
First operation

100 100 0 0 0  
Second operation

100 200 100 100 100  
Third operation

100 200 200 200 100  
Total = 800, Average = 800/5 = 160
'''
def findAverageCandies(jars, noOfInputs):
    #This variable helps in calculating the sum of candies of  all the inputs in the given range 
    sumList=0
    for i in range(noOfInputs):
        #We are splitting the inputs one by one and storing it as a list
        x = [int(i) for i in input().split(' ')]
        #Here the real magic happens. Instead of using another for loop we are taking the difference
        #of the range +1(including the last number i.e 2 to 5 is 5-2 = 3(+1) =4 i.e 2,3,4,5 total 4 jars )
        #Once we find the differnce of the range then we multiply with the candies that are put in to those jars
        #Then we add the total in SumList. This is the same as using for loop with the range of x[0] to x[1] and 
        #adding x[2] to sumList. This line without the for loop has reduced the running time to 0.65 sec max 
        sumList+=((x[1]-x[0]+1)*x[2])
    #Atlast we find the differnce by dividing the sum of all the candies being stored divided  by the number of jars
    #We are typecasting the result as int as asked in the question
    print(int(sumList/jars))

if __name__ == '__main__':
    print("Enter the number of jars and number of inputs:")
    #Getting the first line of input i.e no of jars and no of inputs in a list
    input1= [int(i) for i in input().split(' ') ]
    #Passing the number of jars and  no of inputs 
    findAverageCandies(input1[0],input1[1])