questions=[
    ["Which language was used to create Facebook?","Python","JavaScript","Php","None",4],
    ["Which language was used to create Facebook?","Python","JavaScript","Php","None",4],
    ["Which language was used to create Facebook?","Python","JavaScript","Php","None",4],
    ["Which language was used to create Facebook?","Python","JavaScript","Php","None",4],
    ["Which language was used to create Facebook?","Python","JavaScript","Php","None",4],    
    ["Which language was used to create Facebook?","Python","JavaScript","Php","None",4]

]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
i=0
for i in range (0,len(questions)):
    question=questions[i]
    print(f"Question for  Rs. {levels[i]} is: {question[0]}")
    print(f"a. {question[1]}               b. {question[2]}")
    print(f"c. {question[3]}               d. {question[4]}\n")

    reply=int(input("Enter your answer(1-4) or 0 to quit: "))

    if(reply==0 and i>0):
       money=levels[i-1] 
       break
    elif(i==0):
        money=0
        
    if(reply==question[-1]):
        print(f"Correct Answer, You have won Rs. {levels[i]}")
        print("\n")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong Answer")
        break


print(f"Your take home money is ",money)    