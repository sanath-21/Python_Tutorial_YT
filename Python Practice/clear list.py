# Different ways to clear a list in Python

class User:
    def __init__(self):
        l=[]
        for i in range(5):
            a = input(f"Enter the {i+1} values: ")
            l.append(a)
        print(l)

        l.clear()
        print(l)

u = User()