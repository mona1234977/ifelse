num=int(input("enter the number"))
num1=num%10
num2=(num//10)%10
num3=(num//100)%10
sum=(num1+num2+num3)
if num%sum==0:
    print("harshad number")
else:
    print("not harshad number")