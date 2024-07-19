# Write a program to get the frequency of each letter from the paragraph entered by the user
class User:

    # Taking paragraph input from the user
    def __init__(self):
        self.paragraph = input("Enter Your Paragraph: ")
    
    # getting the frequency of each letter and print the output
    def letterCount(self):
        frequency = {}
        self.paragraph = self.paragraph.upper()
        for i in self.paragraph:
            if i.isalpha():
                if i in frequency:
                    frequency[i] = frequency[i]+1
                else:
                    frequency[i] =  1

        for i in frequency: 
            print(f"{i} : {frequency[i]}")
        

u = User()
u.letterCount()