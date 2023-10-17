list1=[23,33,43,455,65,653,31]

#aggregation function
print("no of elements :",len(list1))
print("maximum element:",max(list1))
print("minimum element :",min(list1))
print("sum of all element:",sum(list1))

#reverse
list1.reverse()
print(list1)


#Sorting
list1.sort()
print("list1:",list1)
#descending
# list1.sort()
# list1.reverse()
list1.sort(reverse=True)
print("list1:",list1)


list2=["amit","aman","vijay","jay","rajan","zil"]
print(list2[0:3])
list2.sort()
print(list2)
list3=list("hello how are you")
print(list3)

print(list2[0])
print(list2[1])
print("============================")
index=0
while index<len(list2):
    print(list2[index])
    index=index+1

print("--------------------------")
#list2.reverse()
for index in range(len(list2)):
    print(list2[index])


print("#################################")
# for each loop
for element in list2:
    print(element)

















