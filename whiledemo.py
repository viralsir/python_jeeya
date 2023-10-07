PASSING_MARKS=35
rollno=int(input("Enter Roll No:"))
name=input("Enter Name :")
maths=int(input("Enter Maths Marks:"))
while maths<0 or maths>100 :
    print("invalid marks")
    maths = int(input("Enter Maths Marks:"))
sci=int(input("Enter Science Marks:"))
while sci<0 or sci>100 :
    print("invalid marks")
    sci = int(input("Enter Science Marks:"))

print("\n output :\n")
print("Roll No:",rollno)
print("Name :",name)
print("Maths :",maths)
print("Science :",sci)

if maths>PASSING_MARKS and sci>PASSING_MARKS :
    print("You are Pass")
    total=maths+sci
    avg=total/2
    print("Total :",total)
    print("Avg :",avg)
    if avg>=90:
        print("Grade :A")
    elif avg>=70:
        print("Grade :B")
    elif avg>=55:
        print("Grade :C")
    else :
        print("Grade :D")
else :
    print("You are Fail")



