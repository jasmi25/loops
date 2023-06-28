#z
#    1
#   212
#  32123
# 4321234
#543212345
a=5
i=1
while i<=a:
    j=1
    while j<=a-i:
        print(" ",end="")
        j=j+1
    b=i
    while b>=1:
        print(b,end="")
        b=b-1
    b=b+2
    while b<=i:
        print(b,end="")
        b=b+1
    print()
    i=i+1
