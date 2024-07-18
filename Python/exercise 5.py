'''Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand 
gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the 
snake beats the water. 
Write a python program to create a Snake Water Gun game in Python using if-else statements. 
Do not create any fancy GUI. Use proper functions to check for win.'''
import random
def check(computer,user):

    if(user==computer):
        print("It's a Draw")

    elif(user=="Snake" and computer =="Water" or user=="Gun" and computer =="Snake" or user=="Water" and computer =="Gun"):
        print("You Won")

    elif(user=="Snake" and computer =="Gun" or user=="Water" and computer =="Snake" or user=="Gun" and computer =="Water"):
        print("You Lose")

    else:
        print("Invalid Input")
        

l=["Snake","Water","Gun"]
computer=random.choice(l)
user= input("Enter Input (Snake/Water/Gun): ")

print(f"Your Choice: {user} \nComputer's Choice:{computer}")
score=check(computer,user)