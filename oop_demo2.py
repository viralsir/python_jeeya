'''

 class : is a collection of related data .
           variable

           def

    object : class variable
             is a instant of class
             is a unique medium to access or get the data which are binds
             to gether in a class.

    refname=classname()

'''

class student :
    rollno=0
    name=""
    maths=0
    sci=0
    eng=0


studentlist=[]

for i in range(2):
    s1=student()
    s1.rollno=int(input("Enter Student Roll No:"))
    s1.name=input("Enter Student Name :")
    s1.maths=int(input("Enter Student Maths Marks:"))
    s1.sci=int(input("Enter Student Science Marks:"))
    s1.eng=int(input("Enter Student English Marks:"))
    studentlist.append(s1)




print("\n output :\n")
for s1 in studentlist:

    print("\n Roll No:",s1.rollno)
    print("\n Name :",s1.name)
    print("\n Maths :",s1.maths)
    print("\n Science :",s1.sci)
    print("\n English :",s1.eng)



















