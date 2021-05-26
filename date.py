date=int(input("enter the date"))
if date==1:
    print("monday")
    date=int(input("enter the date"))
    if date==2:
        print("tuesday")
        date=int(input("enter the date"))
        if date==3:
            print("wednesday")
            date=int(input("enter the date"))
            if date==4:
                print("thursday")
                date=int(input("enter the date"))
                if date==5:
                    print("friday")
                    date=int(input("enter the date"))
                    if date==6:
                        print("saturday")
                        date=int(input("enter the date"))
                        if date==7:
                            print("sunday")
                        else:
                            print("not sunday")
                    else:
                        print("not saturday")
                else:
                    print("not friday")
            else:
                print("not thursday")
        else:
            print("not wednesday")
    else:
        print("not tuesday")
else:
    print("not monday")