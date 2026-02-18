#charity organization donation bonus.

user_donation = int(input("enter your amount for donation"))   #taking input of donation amount from user 
print(user_donation)

maximum_donation = 10000    #condition of bonus
minimum_donation = 5000     #condition of bonus 

if user_donation >= maximum_donation:      #checking the donation amount si eligible for bonus or not .
                                        #if user_donation is greater than or equal to maximum donation then user will get 20% bonus for his donation.

     number = (user_donation )
     percentage = 20
     bonus = (number/100 * percentage)
     print("you got 20% bonus for your donation", bonus)  #user got bonus for his donation 


elif user_donation <= maximum_donation and user_donation >= minimum_donation:   #checking of user donation amount .

    number =(user_donation)
    percentage = 10 
    bonus = (number/100 * percentage)
    print("you got 10% bonus for your donation" , bonus)  #user got bonus for his donation 
else:
    print("no bonus for your donation")    #when user donation is less than minimum donation. 