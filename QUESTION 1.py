a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))


if a>b and a>c:
    print("The largest number is:", a)
elif b>a and b>c:
    print("The largest number is:", b)
elif c>a and c>b:
    print("The largest number is:", c)
elif a==b and a>c:
    print("The largest numbers are equal:", a)
elif a==c and a>b:
    print("The largest numbers are equal:", a)
elif b==c and b>a:
    print("The largest numbers are equal:", b)
else:
    print("All numbers are equal:", a)