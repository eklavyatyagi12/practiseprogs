print("_____________________________________________________________________")
print("_____________________________________________________________________")
print("area of regular triangle")
a = float(input("enter first side     "))
b = float(input("enter seconf side    "))
c = float(input("enter third side     "))

s= ((a+b+c)/2)

area=((s*(s-a)*(s-b)*(s-c))**0.5)

print("area of triangle is : " , area)


k = input("press enter to exit:")

