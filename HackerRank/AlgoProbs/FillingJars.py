'''
Created on Jan 30, 2015

@author: bharath_kalyans
'''
def findAverageCandies(jars, noOfInputs):
    calculateList = [0 for i in range(jars)]
    for i in range(noOfInputs):
        x = [int(i) for i in input().split(' ')]
        for z in range(x[0]-1,x[1]):
            calculateList[z]+=x[2]
    print(int(sum(calculateList)/len(calculateList)))

if __name__ == '__main__':
    
    input1= [int(i) for i in input().split(' ') ]
    mainInput = []
    temp = ()
    #jars = [x for x in range(input1[0]) if True]
    
    findAverageCandies(input1[0],input1[1])