# list1=[23,33,44,65]
# print(list1)
# print(list1[1])
# print(list1[-2])
# print(list1[0:2])
# print(list1[-3:-1])
# print(list1[-3:])
# print(list1[:3])
# print(list1[1:])
# print(list1[:])
#
# list1=[1,'a',23.33]
# print(list1)


# list1=[1,2,3,4,5]
#overwrite value into index or position
# list1[1]=345
# list1[2]='a'
# print(list1)

# list1[1]=int(input("Enter No:"))
# print(list1)

# list1[5]=233
# print(list1)

list1=[]
# append will add elements into next index
list1.append(12)
list1.append(34)
list1.append('amb')
#list1.append(input("Enter value :"))
print(list1)

# # set value at a specific index or position
# list1.insert(1,567)
# list1.insert(1,int(input("Enter Value :")))
# print(list1)
#
#
# #overwrite value into index or position
# list1.__setitem__(2,33)
# print(list1)

#remove value from the list
# list1.remove('amb')
# print(list1)

#remove element by index
# list1.pop()
# list1.pop(1)
# print(list1)

no=int(input("Enter no:"))
if no in list1:
    print(no," is inside the list")
else :
    print(no," is not inside the list")












