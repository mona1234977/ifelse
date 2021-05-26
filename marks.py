marks=int(input("enter the number"))
if marks<25:
    print("f")
    marks=int(input("enter the number"))
    if marks>25:
        print("e")
        marks=int(input("enter the number"))
        if marks>45:
            print("o")
            marks=int(input("enter the number"))
            if marks>50:
                print("a")
                marks=int(input("enter the number"))
                if marks>60:
                    print("b")
                    marks=int(input("enter the number"))
                    if marks>80:
                        print("c")
                    else:
                        print("not c")
                else:
                    print("not b")
            else:
                print("not a")
        else:
            print("not o")
    else:
        print("not e")
else:
    print("not f")