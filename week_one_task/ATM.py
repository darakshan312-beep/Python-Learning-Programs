#ATM withdraw system:

#user's account view.
Available_amount = 10000  
pin = 1234
withdraw_amount = 0
updated_amount = 0

user_pin = int(input("enter your pin:"))   #taking user input of pin for verification.
if user_pin == pin:                        #checking pin is valid or not.
    print("verified")

    withdraw_amount = int(input("enter your withdraw amount:"))     #taking user input of withdraw amount.
    if withdraw_amount <= Available_amount:                         #checking if withdraw amount is available in account or not.
        print("valid amount")
        print("transaction sucessful")
        updated_amount = Available_amount - withdraw_amount         #calculating updated amount after transaction.
        print("updated_amount", updated_amount)        
    else:
        print("invalid amount")                                    #when user enter greater amount than available amount.


else:
        print("invalid pin")                                  #when user enter incorrect pin.
