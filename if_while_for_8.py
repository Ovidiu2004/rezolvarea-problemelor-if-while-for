a=eval(input("a = "))
b=eval(input("b = "))
c=eval(input("c = "))
if (a>0 and b>0 and c>0):
    if ((a<b+c) and (b<a+c) and (c<a+b)):
        if ((a==b==c)):
            print ("triunghi echilateral")
        if (((a==b) and (a!=c)) or ((b==c) and (b!=a)) or ((a==c) and (a!=b))):
            print ("triunghi isoscel")
        if (a!=b!=c):
            print ("triunghi scalen")
    else:
        print("fals")
else:
    print("lungimea nu poate fi negativa") 