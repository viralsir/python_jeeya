sal=float(input("Enter your net salary:"))

if sal<100000 :
    print("No tax will be paid.")

elif sal<300000 and sal>=100000:
    sal=((sal-100000)*0.10)
    print("10% tax will be paid.\n",sal)

elif sal<700000 and sal>300000:
    sal = ((200000) * 0.10)+((sal-300000) * 0.20)
    print("20% tax will be paid.\n",sal)

elif sal<1500000 and sal>700000:
    sal = ((200000) * 0.10)+(400000 * 0.20) + ((sal - 700000) * 0.30)
    print("30% tax will be paid.",sal)

elif sal<2500000 and sal>1500000:
    sal = ((200000) * 0.10)+(400000 * 0.20)+(800000*0.30) + ((sal - 1500000) * 0.40)
    print("40% tax will be paid.",sal)

elif sal>2500000:
    sal = ((200000) * 0.10)+(400000 * 0.20)+(800000*0.30) + (1000000) * 0.40 + (sal-2500000)*0.50
    print("50% tax will be paid.",sal)

else:
    print("Invalid input.")



