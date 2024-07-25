# paragraph =  ["Hello","Wor5d", "Good", "Job","Hii","Be Careful"]
paragraph = [input(f"Enter the {i+1} value: ") for i in range(5)]


for i in paragraph:
    for j in range (0, len(i)):
    
        if((j+1)<len(i)):
            if(i[j]==i[j+1]):
                print(i)