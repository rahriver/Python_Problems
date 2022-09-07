n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

d1 = n1 % n2
d2 = n2 % n1

if d1 == 0 or d2 == 0:
    print('Divisble')
else:
    raise ValueError('Not Divisble')
