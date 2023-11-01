# list1=[n for n in range(1,10)]
#list1=[n**2 for n in range(1,10)]
#list1=[x**2 for x in range(1,10) if x%2==0]
#print(list1)
#
#
# list1=[]
# for x in range(1,10):
#     list1.append(x**2)
maths_list=[12,33,56,77,86,3]
sci_list=[34,44,5,66,76,78]


maths_pass_list=[x for x in maths_list if x>=35]
print(maths_pass_list)
sci_pass_list=[x for x in sci_list if x>=35]
print(sci_pass_list)
math_sci_list=[(x,y) for x,y  in zip(maths_list ,sci_pass_list) if x>=35 and  y >=35]
print(math_sci_list)


