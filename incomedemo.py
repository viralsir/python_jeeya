income=int(input("Enter income:"))
#125000
if income <=100000:
    print("Tax : 0")
elif income <=300000:
    tax=(income%100000)*0.10;
    print("Tax :",tax)
elif income <= 700000:
    tax=20000+(income%300000)*0.20
    print("Tax :", tax)
elif income <=1500000 :
    tax=20000+80000+(income%700000)*0.30
    print("Tax :", tax)
elif income <=2500000:
    tax =100000+(240000)+(income%1500000)*.35
    print("Tax :", tax)
else :
    tax = 100000 + (240000) + (1000000 * 0.35) + (income % 2500000)*.40
    print("Tax :", tax)

