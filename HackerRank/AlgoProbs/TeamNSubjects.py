'''
Created on Jan 29, 2015

@author: bharath_kalyans
'''
import itertools
import operator
def findBest(teamSize,givenSub):
    count =0 
    max= 0 
    
    teams = [i for i in range(teamSize) if True]
    teamCombinations = list(itertools.combinations(teams,2)) 
    for i in teamCombinations:
        x,y=i
        for q in map(operator.add,givenSub[x],givenSub[y]):
            if q>0:
                count+=1
        if count>max:
            max = count
            best = [x,y]
    print()    
                    
    
if __name__ == '__main__':
    subjects = []
    print("Provide the number of students and subjects:")
    input1= input()
    x = [int(i) for i in input1.split(' ') if i]
    for i in range(x[0]):
        #subjects.append(tuple(input()))
        subjects.append([int(x) for x in tuple(input()) if x])
    findBest(x[0],subjects)
