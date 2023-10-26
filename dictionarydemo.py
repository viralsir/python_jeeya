# dict={
#       'first':1,
#       2:"second",
#       "third":3.3433
#       }
# print(dict)
# print(dict['first'])
# print(dict[2])
#
# dict[2]="two"
# print(dict)
# dict["sum"]=343434
# print(dict)
# #print(dict['total'])
#
# dict.__setitem__("rollno",23)
# print(dict)
# print(dict.__getitem__("rollno"))
# print("================")
# #all keys from the dict
# for key in dict.keys():
#     print(key)
# #all values from the dict
# print("======================")
# for value in dict.values():
#     print(value)
#
# #all key value from the dict
#
# print("=====================")
# for key,value in dict.items():
#     print(key,value)


# person={
#         "first_name":"vimal",
#         "last_name":"patel",
#         "phno":3456555
#         }
# person={
#         "first_name":"vimal",
#         "last_name":"patel",
#         "phno":[3456555,34444]
#         }
#
# print(person)
# print(person["phno"])
# print(person["phno"][0])

# person={
#         "first_name":"vimal",
#         "last_name":"patel",
#         "phno":{"home":3456555,"office":34444}
#         }
# print(person["phno"])
# print(person["phno"]["home"])


# student_list =[ {"rollno":1,"name":"vimal","marks":[23,33,44]},
#                 {"rollno":2,"name":"viren","marks":[34,44,55]}
#               ]
#
# print(student_list[0]["rollno"])
# print(student_list[0]["name"])
# print(student_list[0]["marks"][0])
# print(student_list[1]["rollno"])
# print(student_list[1]["name"])


student_list=[]
for i in range(3):
    student={}
    student["rollno"]=int(input("Enter Roll No:"))
    student["name"]=input("Enter Name")
    student_list.append(student)

print(student_list)

for student in student_list:
    for key,value in student.items():
        print(key,value)
    print("==================")

