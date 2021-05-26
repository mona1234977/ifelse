gender=input("enter the gender")
age=int(input("enter the age"))
if gender=="f":
    print("she can do marry")
    if age>18 and age<21:
        print("this is age of girl to marry")
elif age>21 and age<30:
    print("this is age of boys to marry")
    if gender=="m":
        print("boys can marry")
else:
    print("can't do marry")