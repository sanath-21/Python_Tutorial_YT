# RAISE CUSTOM ERRORS

a=input("Enter any value between 5 and 9 or Enter \"quit\": ")

if (a=="quit"):
    print("Exiting...")
elif(a<"5" or a>"9"):
    raise ValueError("Value should be between 5 and 9 or Enter \"quit\" ")
# DEFINING CUSTOM ERRORS
# definition of DEFINING CUSTOM ERRORS is written in the diary
