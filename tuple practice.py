# TUPLES

# tup=(1,12,222,33,55)
# print(type(tup),tup)
# print(tup[0])
# if 33 in tup:
#     print("Yes 33 is present in this tuple ")

# TUPLE METHODS

# countries =("India","Spain","Italy","England","Germany")
# temp=list(countries)
# temp.append("Russia")      #add item
# temp.pop(3)                #remove item
# temp[2]="Finland"          #change item
# countries = tuple(temp)
# print(countries)


# tup1= (1,2,3,4)
# tup2=("Konkani","Kannada","Hindi","English")
# tup=tup1+tup2
# print(tup)

tuple1 =(0,1,2,3,2,3,1,3,2,3)
# res = tuple1.count(3)
# res=tuple1.index(3)
# res=tuple1.index(3,4,8)
res=len(tuple1)
print(res)

# Converting tuple to list and then converting list back to tuple
# tup=(1,5,8,6,9,3)
# my_list=list(tup)
# my_list[0]=0
# new_tuple=tuple(my_list)
# print(new_tuple)