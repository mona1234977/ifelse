age=int(input("enter the age"))
if age>=5:
    print("go school")
    age=int(input("enter the age"))
    if age>=18:
        print("cast vote")
        age=int(input("enter the age"))
        if age>=21:
            print("drive car")
            age=int(input("enter the age"))
            if age>=24:
                print("can marry")
                age=int(input("enter the age"))
                if age>=25:
                    print("can drive")
                else:
                    print("not can drive")
            else:
                print("not can marry")
        else:
            print("not drive car")
    else:
        print("not cast vote")
else:
    print("dont go school")