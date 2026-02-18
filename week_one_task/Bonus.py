#membership discount according to your budget:

print("welcome to the membership program:")  #greeting 

total_bill = int(input("enter your total bill:"))  #taking input of total bill from user.
print(total_bill)

membership_type1 = "premium"    #only two membership types are there : premium or regular.
membership_type2 = "regular"

membership_type = str(input("enter your membership type: premium or regular: ")) #taking input of membership type from user.
print(membership_type)

if membership_type == membership_type1:   #checking membership type and giving discount according to that.
    print("you got 20% discount:")

elif membership_type == membership_type2:
        print("you got 10% discount:")
else:
     print("invalid membership type")     #when user enter any other membership type .