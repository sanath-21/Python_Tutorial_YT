# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

d=input("Do Your Want To CODE/DECODE: ")

a=input("Enter Your Message: ")
if(d=="code"):
# CODING
   
    for i in range (0,len(a)):
            
        if(len(a)>=3):
            r1="abc"
            r2="ghi"
            a=r1+a[1:]+a[0]+r2
            # temp=list(a)
            # temp.pop(0)
            # temp.append(a[0])
            # temp.insert(0,"a")
            # temp.insert(1,"b")
            # temp.insert(2,"c")
            # temp.append("g")
            # temp.append("h")
            # temp.append("i")
            # a=''.join(temp)
            print(a)
            break
        else:
            b=list(a)
            temp=b[0]
            b[0]=b[1]
            b[1]=temp
            a=''.join(b)
            print(a)
            break


# DECODING
elif(d=="decode"):
    for i in range (0,len(a)):
        if(len(a)<3):
            b=list(a)
            temp=b[0]
            b[0]=b[1]
            b[1]=temp
            a=''.join(b)
            print(a)
            break
        else:
            # a=a[3:-3]
            temp=list(a)
            for j in range(3):
                temp.pop(0)
                temp.pop(-1)
            
            a=''.join(temp)
            b=list(a)
            b.insert(0,a[-1])
            b.pop(-1)
            a=''.join(b)

            print(a)
            break

else:
    print("INVALID INPUT")