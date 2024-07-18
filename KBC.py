# Kaun Banega Crorepati

quest=["Which is the National Animal of India?","Which is the National Bird of India?",
        "Who is the Prime Minister of India?","Who is the President of India?",
        "Which Planet is known as Red Planet?","Which is the largest mammal in the world?",
        "What is the capital of India?","How many continents are there in the world?",
        "What is the largest ocean on Earth?","What is the tallest mountain in the world?",
        "Which gas do plants absorb from the atmosphere?","Which animal is known as the \"King of the Jungle\"?"]


ans1=["Tiger","Peacock","Narendra Modi","Draupadi Murmu","Mars","The Blue Whale","Delhi","7","Pacific Ocean",
      "Mount Everest","Carbon Dioxide","Lion"]
earn=[0,1000,2000,5000,12000,24000,50000,100000,300000,1250000,2400000,5000000,10000000]
for i in range (0,12):
    print(quest[i])
    ans=input("Enter your answer: ")
    if(ans==ans1[i]):
        print("Your answer is correct!!! You Earn ",earn[i+1],"\n")
    else: 
        print("Thanks for participating!!!! You Earn ",earn[i],"\n")
        break