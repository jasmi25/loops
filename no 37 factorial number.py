#37.Write a program to print the factorial of a number.
i=1
factorial=1
a=int(input("enter number:-"))
while a>i:
    factorial*=a
    a=a-1
print(factorial)
