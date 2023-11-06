#def to check valid marks
def check_marks(mark,subject):
    while not 0<=mark<=100:
        print("invalid ",subject," marks" )
        mark=int(input("Enter " + subject +" Marks:"))
    return mark


PASSING_MARK=35
#def to check student is pass or fail
def check_pass_fail(maths,sci,eng):
    if maths>=PASSING_MARK and sci>=PASSING_MARK  and eng>=PASSING_MARK:
        return True
    else :
        return False

#display grade of student
def Grade(avg):
    if avg>=90:
        print("Grade :A")
    elif avg>=70:
        print("Grade:B")
    elif avg>=55:
        print("Grade :C")
    else :
        print("Grade :D")

