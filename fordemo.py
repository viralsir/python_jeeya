# for i in range(1,15,5):
#     print(i)

# for i in range(10,1,-1):
#     print(i)


# no=int(input("Enter No:"))
# for value in range(1,11):
#     print(no," * ",value,"=",no*value)



# start=int(input("Enter Start No:"))
# end=int(input("Enter End No:"))
#
# for value in range(start,end+1):
#     print(value)
#     for nvalue in range(1,11):
#         print(value," * ", nvalue," = ",nvalue * value)
#
#     print("=========================================")


# start=int(input("Enter Start No:"))
# end=int(input("Enter End No:"))
#
# while start<=end:
#     value=1
#     while value<=10:
#         print(start," * ",value," = ",start*value)
#         value=value+1
#
#     print("===============================")
#     start=start+1

# no=int(input("Enter No :"))
# factorial=1
# for value in range(1,no+1):
#     factorial=factorial*value;
#
# print("Factorial :",factorial)


no=int(input("Enter No:")) #10
print("Divisor:")
for i in range(1,no+1):
    if  no % i ==0 :
        print(i)

