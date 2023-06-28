#30. Write a program to find the sum of following series
#1 + 8 + 27 …………n terms
i=1
sum=0
a=int(input("enter number"))
while i<=a:
    b=i**3
    sum=sum+b
    i=i+1
print(sum,end=",")
