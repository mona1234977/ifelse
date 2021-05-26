input=input("enter the character")
vowel="aeiou"
special_character="!@#$%^&*><:;"
consonent="bcdfghjklmnpqrstvwxyz"
if input in "vowel":
    print("it is vowel")
elif input in "consonent":
    print("it is consonent")
elif input in special_character:
    print("special character")
elif int(input)> and int(input)<100000000000:
    print("it is number")
else:
    print("not defined")