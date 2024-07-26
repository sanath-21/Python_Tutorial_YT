paragraph = input("Enter a paragraph: ") #get input paragraph from user

for i in range(0, len(paragraph)):
        if((i+1)<len(paragraph)): 
            if(paragraph[i]==paragraph[i+1]):
                print(paragraph[i])