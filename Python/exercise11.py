# DRINK WATER REMINDER


import time
timestamp = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
second = int(time.strftime("%S"))


user = int(input("What Time Do You Get UP?: "))
user2 = int(input("What Time Do You Sleep?: "))


while (user<user2):
    hour = user+2
    user = hour
    if(hour>user2):
        break
    else:
        print(f"Drink Water, It's {hour}:{minute}:{second}")