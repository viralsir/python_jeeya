from student_lib import *

rollno=int(input("Enter Roll No:"))
name=input("Enter Name :")
maths=int(input("Enter Maths Marks:"))
maths=check_marks(maths,"Maths")
sci=int(input("Enter Science Marks:"))
sci=check_marks(sci,"Science")
eng=int(input("Enter English Marks:"))
eng=check_marks(eng,"English")


print("\n output :\n")
print("Roll No:",rollno)
print("Name :",name)
print("Maths :",maths)
print("Science:",sci)
print("English:",eng)
#if check_pass_fail(maths,sci,eng)==True:

if check_pass_fail(maths, sci, eng):
    print("You are Pass")
    total=maths+sci+eng
    avg=total/3
    print(" Total :",total)
    print(" Avg:",avg)
    Grade(avg)
else :
    print("You are fail")



