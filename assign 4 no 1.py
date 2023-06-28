num=int(input("enetrnumber="))
r=sqrt(num)
i=1
while i<r:
    if num%i==0:
        print(i)
        print(num/i)
    i+=1
