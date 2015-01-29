'''
Created on Jan 29, 2015

@author: bharath_kalyans
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
    
    
