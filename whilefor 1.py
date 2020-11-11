n=eval(input('introduceti un numar'))
if n==31:
    print('ianuarie,martie,mai,iulie,august,octombrie,decembrie')
elif n==30:
    print('aprilie,iunie,septembrie,noiembrie')
elif n<28:
    print('eroare')
else:
    print('februarie')