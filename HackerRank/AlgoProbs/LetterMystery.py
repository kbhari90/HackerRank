'''
Created on Jan 29, 2015

@author: bharath_kalyans

Problem Statement

James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows 2 rules:

(a) He can reduce the value of a letter, e.g. he can change 'd' to 'c', but he cannot change 'c' to 'd'. 
(b) In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter becomes 'a'. Once a letter has been changed to 'a', it can no longer be changed.

Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome. 


Input Format 
The first line contains an integer T, i.e., the number of test cases. 
The next T lines will contain a string each. The strings do not contain any spaces.

Output Format 
A single line containing the number of minimum operations corresponding to each test case.

Constraints 
1 <= T <= 10
1 <= length of string <= 104 
All characters are lower case English letters.

Sample Input #00

4
abc
abcba
abcd
cba
Sample Output #00

2
0
4
2
Explanation

For the first test case, abc -> abb -> aba.
For the second test case, abcba is already palindromic string.
For the third test case, abcd -> abcc -> abcb -> abca = abca -> abba.
For the fourth test case, cba -> bba -> aba.
'''

#For HackerRank IDE we have to just give input() to get the inputs automatically
inputLength = int(input("Enter length of inputs: "))
givenStrings =[]
print("Enter the letters: ")
for i in range(inputLength):
    givenStrings.append(input())

def convertToPalindrome(i):
    countChanges = 0
    left = []
    right = []
    
    if i:
        if i == "".join(reversed(i)):
            return countChanges
        else:
            i = list(i)           
            if len(i)%2==0:
                left=(i[:int((len(i)/2))])
                right=(i[int(len(i)/2):])
                right.reverse()
                
            else:
                left = (list(i[:int(len(i)/2)]))
                right = (list(i[int(len(i)/2)+1:]))
                right.reverse()
                
            for x in range(len(left)):
                if ord(left[x])>ord(right[x]):
                    while ord(left[x])!=ord(right[x]):
                        left[x] = chr(ord(left[x])-1)
                        countChanges+=1
                elif ord(left[x])<ord(right[x]):
                    while ord(left[x])!=ord(right[x]):
                        right[x] = chr(ord(right[x])-1)
                        countChanges+=1
                
            return countChanges   
            
           
for i in givenStrings:
    print(convertToPalindrome(i))
    
    
