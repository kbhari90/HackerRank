'''
Created on Jan 29, 2015

@author: bharath_kalyans
********************
Problem Statement
********************

Dothraki are planning an attack to usurp King Robert from his kingdom. King Robert learns of this conspiracy from Raven and plans to lock the single door through which an enemy can enter his kingdom.

door

But, to lock the door he needs a key that is an anagram of a certain palindrome string.

The king has a string composed of lowercase English letters. Help him figure out if any anagram of the string can be a palindrome or not.

Input Format 
A single line which contains the input string

Constraints 
1<=length of string <= 10^5 
Each character of the string is a lowercase English letter.

Output Format 
A single line which contains YES or NO in uppercase.

Sample Input : 01

aaabbbb
Sample Output : 01

YES
Explanation 
A palindrome permutation of the given string is bbaaabb. 
'''


def checkPal(givenString):
    #count is for counting the number of characters that have odd occurances(only one occurance is permissable to make the string a palindrome)
    count= 0
    #this list stores the characters which have been cheked for palindrome so we can skip it in the loop if it occurs again
    pal = []
    
    for i in range(len(givenString)):
        #Checking if the character is already checked, if so we continue the loop
        if givenString[i] in pal:
            continue
        else:
            #we are counting the occurances of the characters
            stringCount =  givenString.count(givenString[i])
            #checking if count is even number
            if stringCount%2==0:
                pal.append(givenString[i])
                continue
            else:
                #if its an odd number then we increase the count by 1
                count+=1
                #adding the checked character in to pal
                pal.append(givenString[i])
                #checking if the number of odd occurances has surpassed 1
                if count>1:
                    return 'NO'
    return 'YES'
#We are getting the input as list
givenString = list(input())
print(checkPal(givenString)) 