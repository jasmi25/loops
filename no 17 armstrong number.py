#17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is
#equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)
a=input("enter number:-")
i=0
arm=0
while i<len(a):
    b=a[i]
    c=(int(b)**3)
    arm=c+arm
    i=i+1
print(arm)
if int(a)==arm:
    print("its armstrong number")
else:
    print("its not arm stron number")
