# Write a Program which should print the range of numbers entered by user in which if the number is divisible by 3 then print "FIZZ" if the number is divisible by 5 then print "BUZZ" and if the number is divisible by both then print 

class User:

#  Takes the input from user the range of numbers 
    def __init__(self):
        self.num = int(input("Enter the range of numbers: "))

# Computes the logic and prints "Fizz", "Buzz" or "Fizz-Buzz" accordingly
    def getResult(self):
        for i in range(1, (self.num+1)):
            if (i%3==0 and i%5==0):
                print ("FIZZ-BUZZ")
            elif (i%3==0):
                print("FIZZ")
            elif (i%5==0):
                print("BUZZ")
            else: 
                print(i)

u = User()
u.getResult()
