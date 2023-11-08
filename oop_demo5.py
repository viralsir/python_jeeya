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
from student_lib import *


class student :

    #using constructor
    def __init__(self):
        self.rollno=0
        self.name=""
        self.maths=0
        self.eng=0
        self.sci=0

    def entry(self):
        self.rollno = int(input("Enter Student Roll No:"))
        self.name = input("Enter Student Name :")
        self.maths = int(input("Enter Student Maths Marks:"))
        self.maths = check_marks(self.maths,"Maths")
        self.sci = int(input("Enter Student Science Marks:"))
        self.sci = check_marks(self.sci,"Science ")
        self.eng = int(input("Enter Student English Marks:"))
        self.eng= check_marks(self.eng,"English ")

    def view(self):
        print("\n Roll No:", self.rollno)
        print("\n Name :", self.name)
        print("\n Maths :", self.maths)
        print("\n Science :", self.sci)
        print("\n English :", self.eng)
        if check_pass_fail(self.maths,self.sci,self.eng):
            print("you are pass")
            total=self.maths+self.sci+self.eng
            avg=total/3
            print("Total :",total)
            print("Avg :",avg)
            Grade(avg)

        else :
            print("You are Fail ")

studentlist=[]

for i in range(2):
    s1=student()
    s1.entry()
    studentlist.append(s1)




print("\n output :\n")
for s1 in studentlist:
    s1.view()



















