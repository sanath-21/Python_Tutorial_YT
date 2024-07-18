# MAP, FILTER & REDUCE

# MAP
# def cube(x):
#     return x**3
# print(cube(2))

# l=[1,2,4,6,4,3]
# Before using map function
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)

# Using map function
# newl=list(map(cube,l))  #taking funjcation as an argument
# newl=list(map(lambda x: x**3,l)) #using lambda function as argument
# print(newl)


# FILTER

# def filter_function(a):
#     return a>2


# l=[1,2,4,6,4,3]
# newnewl= filter(filter_function,l) #taking funjcation as an argument
# newnewl= filter(lambda x: x>2,l) #using lambda function as argument
# print(list(newnewl))


# REDUCE
# from functools import reduce

# numbers=[1,2,3,4,5]

# # Calculate the sum of the numbers using reduce function
# sum=reduce(lambda x,y: x+y,numbers)
# print(sum)