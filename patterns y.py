#y)
#      *
#    * * *
#  * * * * *
#* * * * * * *
i=1
a=4
b=1
while i<=a:
    j=1
    while j<=4-i:
        print(" ",end="")
        j=j+1
    k=1
    while k<=b:
        print("*",end="")
        k=k+1
    b=b+2
    print()
    i=i+1
