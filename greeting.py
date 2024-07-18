import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)

# hour=int(input("Enter Hour: "))
hour=int(time.strftime('%H'))
print(hour)

# minute=int(input("Enter Minute: "))
minute=int(time.strftime('%M'))
print(minute)

# seconds=int(input("Enter Seconds: "))
seconds=int(time.strftime('%S'))
print(seconds)

name=input("Enter Name: ")
if(hour<12 and hour>=4):
    print("Good Morning "+name)
elif(hour>=12 and hour<16):
    print("Good Afternoon "+name)  
elif( hour>=16 and hour<20):
    print("Good Evening "+name)    
else:
    print("Good Night "+name)