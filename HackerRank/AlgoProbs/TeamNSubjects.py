'''
Created on Jan 29, 2015

@author: bharath_kalyans
#################
Problem Statement
#################

You are given a list of N people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic or they are not. Find out the maximum number of topics a 2-person team can know. And also find out how many teams can know that maximum number of topics.

Note Suppose a, b and c are 3 different people then (a,b) and (b,c) are counted as two different teams.

Input Format

The first line contains two integers N and M separated by a single space, where N represents the number of people, and M represents the number of topics. N lines follow.
Each line contains a binary string of length M. If the ith line's jth character is 1, then the ith person knows the jth topic and doesn't know the topic otherwise.

Output Format

On the first line, print the maximum number of topics a 2-person team can know. 
On the second line, print the number of 2-person teams that can know the maximum number of topics. 

Constraints 
2 <= N <= 500 
1 <= M <= 500

Sample Input

4 5
10101
11100
11010
00101
Sample Output

5
2
Explanation 
(1, 3) and (3, 4) know all the 5 topics. So the maximal topics a 2-person team knows is 5, and only 2 teams can achieve this.
'''


def findBest(teamSize,givenSub):
    #Variable for storing the maximum  number of subjects known by a person
    max= 0 
    #variable to store the teams with maximum subjects known
    best = []
    #From the teamsize we create a list i.e if 4 then 0,1,2,3 is the list val
    teams = [i for i in range(teamSize) if True]
     
    #In the below two loops we are finding the combinations of the given list
    for m in teams:
        for n in teams:
            #Here we are checking n<=m so that the values dont repeat i.e 1,2 and 2,1 which is permutation and not combination
            if n<=m:
                pass
            else:
                x,y=m,n
                #varible to count the no f subjects know by the combination of teams
                counts= 0
               
                #Here is the real magic happens ,without this line the test were giving Timeout error
                #The below implementation is that we are converting the string inputs of givensubject into
                #binary integers and we are comparing using the OR operator and atlast we are converting the binary in to the real input by using bin()
                #and then we are counting the whole output for occurance of 1. This line has masde the program fast
                #Before this line the code was: #counts=sum(q>0 for q in map(operator.add,givenSub[x],givenSub[y]) )
                #that code was too slow
                counts = bin(int(givenSub[x],2)|int(givenSub[y],2)).count('1')
                if counts>max:
                    #We are checking if the new count is the max if so we are equating counts to max
                    max = counts
                    #Once we find a new max we empty the best list and append the new team that knows max subject
                    best = []
                    best.append([x,y])
                #We are checking if the counts are same as max in which case there is another team with the same max known subjects
                elif counts==max:
                    best.append([x,y])

    print(max) 
    #We print the teams that know max subjects
    print(len(best))
                    
    
if __name__ == '__main__':
    #List to store the subjects known data
    subjects = []
    #getting the first line of input: no of people and no of subjects
    print("Enter the no of people and no of subjects")
    input1= input()
    #Converting the first input into list of integers
    print("Enter the categization of subjects known")
    x = [int(i) for i in input1.split(' ') if i]
    for i in range(x[0]):
        #Getting the subjects as strings
        subjects.append(input())
        
    #Passing the no of people and the categorization of subjects
    findBest(x[0],subjects)