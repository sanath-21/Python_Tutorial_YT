# 3) Write a Python code to find the Minimum of these two numbers.

def minimum():
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))

    if num1>num2:
        print(f"{num2} is less than {num1}")
    elif num1==num2:  
        print(f"{num1} is equal to {num2}") 
    else:
        print(f"{num1} is less than {num2}")

minimum()