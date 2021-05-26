atm=input("enter the atm")
if atm==("chip side"):
    print("start transaction")
    balance=int(input("enter the amount"))
    if balance<20000:
        print("balance is available")
        language=input("enter the language")
        if language=="hindi" or language=="english" or language=="others":
            print("select language")
            account=input("enter the account")
            if account=="saving account" or account=="current account":
                print("select account")
                pin=int(input("enter the pin"))
                if pin==1234:
                    print("pin is correct")
                    amount=int(input("enter the amount"))
                    if amount>0 and amount<10000:
                        print("your transaction is completed")
                        receipt=input("enter yes or no")
                        if receipt=="yes":
                            print("take your receipt")
                            privacy=input("enter the privacy yes or no")
                            if privacy=="yes":
                                print("thank you")
                            else:
                                print("no")
                        else:
                            print("no")
                    else:
                        print("amount is not available")
                else:
                    print("incorrect pin")
            else:
                print("account not found")
        else:
            print("not defined")
    else:
        print("balance not available")
else:
    print("sorry")