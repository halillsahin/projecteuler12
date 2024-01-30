def üçgen_sayılar(n):
    return (n*n+n)/2
a=1
while True:
    b=0
    a+=1
    c=üçgen_sayılar(a)+1
    for i in range(1,int(c**0.5+1)):
        if (üçgen_sayılar(a))%i==0:
            b+=2
    if b>500:
        print(üçgen_sayılar(a))
        break       
    else:
        b=0 