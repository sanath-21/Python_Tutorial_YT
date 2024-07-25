# Check if element exists in list in Python

class User:

    def __init__(self):
            
        self.l = []
        for i in range(5):
            self.a = input(f"Enter {i+1} values: ")
            self.l.append(self.a)
        
        # Take input from use the value you want to search
        self.b = input("Enter the value you want to search: ")
    
    # this function checks if the element exits in the list or not
    def compute(self):
        if self.b in self.l:
            print(f"Yes {self.b} exists in {self.l}")
        else:
            print(f"No {self.b} does not exist in {self.l}")


u = User()
u.compute()