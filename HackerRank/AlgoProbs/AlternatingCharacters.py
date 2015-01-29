'''
Created on Jan 29, 2015

@author: bharath_kalyans
#################
Problem Statement
#################

Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.

Input Format 
The first line contains an integer T i.e. the number of test cases. 
Next T lines contain a string each.

Output Format 
For each test case, print the minimum number of deletions required.

Constraints

1<=T<=10 
1<=lengthofString<=105 

Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Sample Output

3
4
0
0
4
Explanation

AAAA=>A, 3 deletions
BBBBB=>B, 4 deletions
ABABABAB=>ABABABAB, 0 deletions
BABABA=>BABABA, 0 deletions
AAABBB=>AB, 4 deletions
'''
def findDeletions(givenStrings):
    #This varible save the number of deletions
    deletions =0
    for i in  givenStrings:
        #Taking each string and looping into each character of the string
        for x in range(len(i)):
            #Checking if the last character has reaches as it cant be compared to any other characres i.e x+1
            #so we are breaking out of the loop
            if x==len(i)-1:
                break
            #Checking if the next character is same, if so we add 1 to the deletions
            if i[x]==i[x+1]:
                deletions+=1
        print(deletions)
        #Atlast we make deletions as 0 for the next character in the loop
        deletions = 0 
        

if __name__ == '__main__':
    #List to get the input strings
    givenStrings = []
    print("Give the limit:")
    #variable to get the limit 
    t= int(input())
    print("Enter the strings:")
    for i in range(t):
        givenStrings.append(input())
    findDeletions(givenStrings)