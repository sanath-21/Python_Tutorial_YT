class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod #using static method decorator no need to use self as parameter in the method
    def add(a,b):
        return a+b 

# result=Math.add(1,2)
# print(result)

# a=Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)
# print(a.add(7,2))