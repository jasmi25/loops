#h
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
i=1
n=5
while i<=n:
    a=1
    while a<=n-i:
        print(" ",end="")
        a=a+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1

    
