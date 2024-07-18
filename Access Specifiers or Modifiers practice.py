# PUBLIC ACCESS MODIFIERS/SPECIFIERS
# class Employee:
#     def __init__(self):
#         self.name="Harry"

# a=Employee()
# print(a.name)

# PRIVATE ACCESS MODIFIERS/SPECIFIERS
# class Employee:
#     def __init__(self):
#         self.__name="Harry"

# a=Employee()
# print(a.__name) #cannot be accessed directly
# print(a._Employee__name)#can be accessed indirectly (NAME MANGLING)

# PROTECTED ACCESS MODIFIERS/SPECIFIERS
# class Student:
#     def __init__(self):
#         self._name="Harry"
        
#     def _funName(self): #protected method
#         return "CodeWithHarry"

# class Subject(Student): #inherited class
#     pass

# obj = Student()
# obj1=Subject()

# # calling by object of class Student
# print(obj._name)
# print(obj._funName())
# # calling by object of a class Subject
# print(obj1._name)
# print(obj1._funName())