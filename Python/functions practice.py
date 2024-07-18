def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
      print(a," is greater than ",b)
    elif(a==b):
       print(a," and ",b," both are equal")
    else:
       print(b," is greater than ",a)
def isLesser(a,b):
   pass

a=9
b=8
calculateGmean(a,b)
isGreater(a,b)
c=8
d=7
calculateGmean (c,d)
isGreater(c,d)