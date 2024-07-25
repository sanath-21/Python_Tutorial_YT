# 2) Write a Python code to find the Maximum of these two numbers.

def maximum():
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))

    if num1>num2:
        print(f"{num1} is greater than {num2}")
    elif num1==num2:  
        print(f"{num1} is equal to {num2}") 
    else:
        print(f"{num2} is greater than {num1}")

maximum()