rollno=[]
name=[]
maths=[]
sci=[]
eng=[]


i=1
while i<=3:
    rollno.append(int(input("Enter Roll no:")))
    maths.append(int(input("Enter Maths Mark:")))
    sci.append(int(input("Enter Science Mark:")))
    eng.append(int(input("Enter English Mark:")))
    i=i+1

print("\n output :\n")
for r,m,s,e in zip(rollno,maths,sci,eng):
    print("===============================")
    print("Roll NO:",r)
    print("Maths :",m)
    print("Science :",s)
    print("English:",e)
    if m>=35 and s>=35 and e>=35 :
        print("You are Pass")
    else:
        print("You are Fail")



