#22. Write a program to accept 10 numbers from the user and display it’s average
i=1
b=int(input("enter number:-"))
sum=0
while i<=b:
    a=int(input("enter number"))
    sum=sum+a
    i=i+1
average=sum//b
print(average)
