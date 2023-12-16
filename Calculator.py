def sum(x,y):
    return x+y

def product(x,y):
    return x*y

def exponent(x,y):
    z=1
    for i in range(y):
        z=z*x
    return z

def division(x,y):
    return x/y

x=int(input("Your first number= "))
X=input("Enter Operator ")
y=int(input("Your second number= "))


if X=="+":
    print(sum(x,y))
elif X=="*":
    print(product(x,y))
elif X=="^":
    print(exponent(x,y))
elif X=="/":
    print(division(x,y))
else:
    print("Operation Error")