#32. Write a program to find the sum of following series:
#S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
i=2
b=1
sum=1
a=int(input("enter number:-"))
while i<=a:
    if i%2==0:
        b=i**2
        sum=sum+b
        print(sum,end="")
    else:
        print("-",end="")
    i=i+1
