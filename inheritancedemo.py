''''
 inheritance :
 is the proccess by which object of one class can access or get the
 properties of object of another class.


 Class A
      noA

 class B(A)
       noB


 a1=A()
 b1=B()

 b1.noB
 b1.noA

 a1.noA
 a1.noB

 category of inheritance :-
 1)Single Inheritance :-
     one object can access the properties of only one object at a time.

     A  Personal_Info (Parent class,base class, super class)
     |  |
     B  Employee    (child class , derived class ,sub class)

2) Multilevel Inheritance  :- continous chain of single inheritance .

       A
       |
       B
      |
      C
      |
      D




'''

class Personal_Info:
    id=0
    name=""
    phno=""

    def setPersonl_Info(self):
        self.id=input("Enter Id:")
        self.name=input("Enter Name:")
        self.phno=input("Enter Phno:")

    def getPersonal_Info(self):
        print("Id :",self.id)
        print("Name :",self.name)
        print("Phno:",self.phno)

class Employee(Personal_Info):
    salary=""

    def setSalary(self):
        self.salary=int(input("Enter Salary :"))

    def getSalary(self):
        print("Salary :",self.salary);




employee=Employee();
employee.setPersonl_Info()
employee.setSalary()

employee.getPersonal_Info()
employee.getSalary()








