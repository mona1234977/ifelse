day=input("enter the day")
if day=="sunday":
    print("go outside")
    place=input("enter the place")
    if place=="hospital":
        print("go hospital")
        senior=input("enter the permission")
        if senior=="yes":
            print("permission granted")
            safety=input("enter the safety precaution")
            if safety=="mask":
                print("go with mask,sanitizer")
                time=int(input("enter the time"))
                if time<6:
                    print("come before 6 at evening")
                    reason=input("enter the work")
                    if reason=="ng work":
                        print("dont go in quarentine")
                    else:
                        print("go to quarentine")
                else:
                    print("come after 6 at evening")
            else:
                print("dont go with mask")
        else:
            print("permission not granted")
    else:
        print("dont go in hospital")
else:
    print("dont go outside")
