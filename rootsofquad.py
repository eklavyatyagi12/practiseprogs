import cmath

print("--------------------------------------------------------")
print("the general form of quadratic equation is :  Ax^2 + Bx + C")
a = int(input("ENTER A:   "))

if(a!=0):
    b = int(input("ENTER B:   "))
    c = int(input("ENTER C:   "))

    d = (b**2) - (4*a*c)

    sol2 = (-b+cmath.sqrt(d))/2*a
    sol1 = (-b -cmath.sqrt(d))/2*a

    print('The solution are {0} and {1}'.format(sol1,sol2))
else :
    print("A CANNOT BE ZERO")

k= input("press enter to exit")



