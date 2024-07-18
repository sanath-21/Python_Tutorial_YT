# EXAMPLE OF HYBRID INHERITANCE
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass

# CODE
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print(f"Address: {self.address}")

class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration
    
    def show_details(self):
        print(f"Program Name: {self.program_name}")
        print(f"Duration: {self.duration}")
    
class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program
    
    def show_details(self):
        Person.show_details(self)
        self.program.show_details()

program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()