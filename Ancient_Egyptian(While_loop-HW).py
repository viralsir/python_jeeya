a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
sum=0
while b!=0:
    print("a:",a ," and b:",b)
    if (b % 2 != 0):
        sum = sum + a;
    a *=2;
    b //= 2;

print("sum is:",sum)
