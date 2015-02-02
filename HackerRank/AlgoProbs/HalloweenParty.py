'''
Created on Feb 2, 2015

@author: bharath_kalyans
#################
Problem Statement
#################

Alex is attending a Halloween party with his girlfriend Silvia. At the party, Silvia spots a giant chocolate bar. If the chocolate can be served as only 1 x 1 sized pieces and Alex can cut the chocolate bar exactly K times, what is the maximum number of chocolate pieces Alex can cut and give Silvia?

Input Format
The first line contains an integer T, the number of test cases. T lines follow.
Each line contains an integer K

Output Format
T lines. Each line contains an integer that denotes the maximum number of pieces that can be obtained for each test case.

Constraints
1<=T<=10
2<=K<=107

Note 
Chocolate must be served in size of 1 x 1 size pieces. 
Alex can't relocate any of the pieces, nor can he place any piece on top of another.

Sample Input #00

4
5
6
7
8
Sample Output #00

6
9
12
16
Explanation
The explanation below is for the first two test-cases. The rest of them follow a similar logic.

For the first test-case where K = 5,You need 3 Horizontal and 2 vertical cuts. 
halloweenboard For the second test-case where K = 6,You need 3 Horizontal and 3 vertical cuts.
'''
def howManyChocolates(noOfInput):
    #This variable stores the maximum number of chocolate pieces i.e the maximum value of the multiplication done between the digits of a given input
    #i.e if 6 then 3*3 = 9 3 and 3 makes 6 as well as its multiplication makes 9 which is the max value from the digits that make the input value 
    maxPieces = 0
    print("Enter the inputs:")
    for i in range(noOfInput):
        x= int(input())
#         for z in range(1,int(x/2)+1):
        #the maximum value is always the middle number of the given input  * the rest of the numbers i.e 6 :- 3*3 7:- 3*4
        z = int(x/2)
        maxPieces = (x-z)*z
        print(maxPieces)
if __name__=='__main__':
    #we are getting the number of inputs
    print("Enter the number of inputs:")
    noOfInput = int(input())
    howManyChocolates(noOfInput)