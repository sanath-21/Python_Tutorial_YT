#  Sum of values in List

n = int(input("Enter the range of numbers you want to Enter: "))
number = [int(input(f"Enter {i+1} value: ")) for i in range(n)]
sum=0
for i in number:
    sum = sum + i

print(f"The list of number is: {number}")
print(sum)