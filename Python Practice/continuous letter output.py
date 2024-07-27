# paragraph =  ["Hello","Wor5d", "Good", "Job","Hii","Be Careful"]

paragraph = [input(f"Enter the {i+1} value: ") for i in range(5)] #get input values from user


for i in paragraph:   #store each word in i
    for j in range (0, len(i)): #will iterate from 0 to len of each word
    
        if((j+1)<len(i)): 
            if(i[j]==i[j+1]):
                print(i)