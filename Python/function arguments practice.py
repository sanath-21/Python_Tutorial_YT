# def average(a=9,b=1):
#     print("The average is",(a+b)/2)

# average(1,5)

# def name(fname, mname="Jhon",lname="Whatson"):
#     print("Hello",fname,mname,lname)
# name("Amy", "Jain")

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is ",sum/len(numbers))
    return sum/len(numbers)


c=average(3,3)
print  (c)