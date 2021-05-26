a=int(input("enter the number"))
b=int(input("enter the number"))
c=input("operator")
if c=="+":
    print("addition",a+b)
elif c=="-":
    print("subtration",a-b)
elif c=="*":
    print("multiplication",a*b)
elif c=="%":
    print("module",a%b)
elif c=="/":
    print("devide",a/b)
else:
    print("not define")