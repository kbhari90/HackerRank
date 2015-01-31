'''
Created on 31-Jan-2015

@author: bharath_kalyans
#################
Problem Statement
#################

Little Bob loves chocolates, and goes to a store with $N in his pocket. The price of each chocolate is $C. The store offers a discount: for every M wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?

Input Format: 
The first line contains the number of test cases T(<=1000). 
T lines follow, each of which contains three integers N, C and M

Output Format: 
Print the total number of chocolates Bob eats.

Constraints: 
2<=N<=105 
1<=C<=N 
2<=M<=N

Sample input

3
10 2 5
12 4 4
6 2 2
Sample Output

6
3
5
Explanation 
In the first case, he can buy 5 chocolates with $10 and exchange the 5 wrappers to get one more chocolate. Thus, the total number of chocolates is 6.

In the second case, he can buy 3 chocolates for $12. However, it takes 4 wrappers to get one more chocolate. He can't avail the offer and hence the total number of chocolates remains 3.

In the third case, he can buy 3 chocolates for $6. Now he can exchange 2 of the 3 wrappers and get 1 additional piece of chocolate. Now he can use his 1 unused wrapper and the 1 wrapper of the new piece of chocolate to get one more piece of chocolate. So the total is 5.
'''
def findChocEaten(tc):
    for i in range(tc):
        x = [int(z) for z in input().split(' ')]
        #we are claculating the chocolates in hand by dividing no of chocolates with money in hand
        wrappersInHand = int(x[0]/x[1])
        #checking if wrappers in hand are less than the required wrappers to get another chocolate
        if wrappersInHand<x[2]:
            #if so we print the output staraightaway as we dont have enough wrappers to exchange for 
            #another chocolate
            print(wrappersInHand)
        #Checking if wrappersinhand are equal to the exchange offer , if so we print wrappersinhand + 1 chocolate that we got in exchange 
        elif wrappersInHand==x[2]:
            print(wrappersInHand+1)
        else:
            #This variable has the number of chocloates consumed
            count =wrappersInHand
            #while wrappers in hand are greater than or equal to the exchange offer wrappers
            while wrappersInHand>=x[2]:
                #we exchange the wrappers for a chocolate, so we reduce the wrappersinhand with the amt of wrappers exchanged
                wrappersInHand-=x[2]
                #Here we count the number of chocolates eaten, 1 more that we got from exchange offer
                count+=1
                #one more wrapper also increases as we got one from the exchange offer
                wrappersInHand+=1
            print(count)
if __name__=='__main__':
    print("Enter the number of test cases:")
    #Getting the first input and passing it to the functions
    tc = int(input())
    print("Enter no of choc , price and wrapper count for discount:")
    findChocEaten(tc)
        