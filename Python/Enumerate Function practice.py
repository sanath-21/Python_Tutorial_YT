marks = [12, 56, 32, 98, 12, 45, 1, 4]
# Non Enumerated Code
# index = 0
# for mark in marks:
#     print(mark)
#     if( index == 3):
#         print("Harry, awesome!")
#     index +=1

# Enumerated Code

for index, mark in enumerate(marks, start=1):
    print(index, mark)
    if( index == 3):
        print("Harry, awesome!")