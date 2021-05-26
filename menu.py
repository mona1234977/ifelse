day=input("enter the day")
meal=input("enter the meal")
if day=="monday":
    if meal=="breakfast":
        print("dalia")
    elif meal=="lunch":
        print("dal chawal")
    else:
        print("roti sbji")
elif day=="tuesday":
    if meal=="breakfast":
        print("poha")
    elif meal=="lunch":
        print("rajma chawal")
    else:
        print("roti bhindi")
elif day=="wednesday":
    if meal=="breakfast":
        print("parathe")
    elif meal=="lunch":
        print("pulav")
    else:
        print("matar paneer")
else:
    print("momos")