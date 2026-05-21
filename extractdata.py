value=int(input("Enter number"))
count=0
for i in range(1,value+1):
    if value%i==0:
        count+=1
if count ==2:
    print("prime number")
else:
    print("not prime")