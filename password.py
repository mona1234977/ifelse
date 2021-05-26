name=input("enter the name")
password=input("enter the password")
if name=="mona":
    if password=="mona1234":
        print("you have login successfully")
    else:
        print("wrong password")
elif name!="mona" and password=="mona1234":
    print("wrong name")
elif name=="mona" and password!="mona1234":
    print("wrong password")
elif name!="mona" and password!="mona1234":
    print("create new account")
else:
    ("not defined")