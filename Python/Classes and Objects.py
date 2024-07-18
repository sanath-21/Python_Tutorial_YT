class Person:
    name="Harry"
    occupation = "Software Developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name="Shubham"
# a.occupation="Accountant"
# print(f"{a.name}\n{a.occupation}")
a.info()