#day 04 of python programming practice .
# conditions (if , else )    # result always in boolean data type .


x = int(input("enter your age: "))
if x >= 18:                         #if condition used when we have only one condition true or false 
    print("you are eligible for vote ")
else:
    print("you are not eligible for vote")  #else condition is used when we have two contidions true and false 


 #practice tasks:
                     #even or odd
no = int(input("enter any number:"))    
if no  %  2 == 0 :            # condition is that , if the given number is divisible by 2 then only it is considered even otherwise it is an odd number.
    print("even")             
else:
    print("odd") 

                  #pass or fail
marks = int(input("enter your marks:"))     
if marks >= 75:
    print("pass")
else:
     print("fail")


                       #password checker.
password = int(input("enter your password:"))
if password == 1234567:
    print("access granted")
else :
     print("try again")



# day 05 of python programming practice 
# elif means else if condition :  with the help of elif we can use multiple conditions in our program.

#grades calculator
grades = int(input("enter your marks:"))
if grades >= 80:
     print("A+")
elif grades <= 70:
     print("A")   
elif grades <= 60:
     print("B")
elif grades <= 50:
     print("C")

else:
     print("fail")



 #age category:
age = int(input("enter your age please:"))
if age >= 18:
     print("an adult")
elif age >= 10:
     print("a teenage")
else:
     print("a child")


# #weekend checker
weekend = input("enter the day of today:")

if weekend == "sunday" or weekend == "saturday":
     print("today is weekend")

else:
     print("weekday")


#login checker:
email = "daru@gmail.com"
password = 123
login = input("enter your email:")
if login == email:
    print("valid email:")
    Pass = int(input("enter your password:"))
    if Pass == password:
        print("correct password:")
        print("access granted")
    else:
         print("invalid password , try again")
else:
    print("invalid email , try again")