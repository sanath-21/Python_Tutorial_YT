a=input("Enter Your Message: ")
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