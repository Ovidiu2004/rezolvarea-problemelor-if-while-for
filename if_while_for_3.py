import math
a=int(input("a="))
b=int(input("b="))
if a>b or a==b:
    print("in conditie se cere ca a sa fie < b")
else:
    i=round(math.log(b,a))
    if a**i==b:
        print("b este o putere")
    else:
        print("b nu este o putere")