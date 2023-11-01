# set1={12,23,44,45,66,"vimal",3434.343}
# print(set1)
# #
# # for element in set1:
# #     print(element)
#
# #set1.add(345)
# set1.add(input("Enter value :"))
# print(set1)
#
# set1.remove(23)
# print(set1)

set1={1,2,3,4,5}
set2={3,4,5,6,7,8}

#intersection
set3= set1 & set2
set4=set1.intersection(set2)
print("intersection :",set3)
print("intersection:",set4)

# difference
set3= set1 - set2
set4= set2.difference(set1)

print("difference:",set3)
print("difference:",set4)


#union
set3=set1 | set2
set4=set1.union(set2)

print("union :",set3)
print("union :",set4)

#symentric diff

set3=set1 ^ set2
set4=set1.symmetric_difference(set2)
print("symmetric diff :",set3)
print("symmetric diff :",set4)


















