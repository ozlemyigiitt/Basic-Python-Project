a=int(input("Enter a number for a"))
b=int(input("Enter a number for b"))
c=int(input("Enter a number for c"))
while a>0 and b>0 and c>0:
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c>b:
        print(c)
    a=int(input("Enter a number for a"))
    b=int(input("Enter a number for b"))
    c=int(input("Enter a number for c"))
