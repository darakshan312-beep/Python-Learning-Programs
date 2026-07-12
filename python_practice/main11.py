# #week : 03                   #day : 05
# #variable scope(where a variable can be accessed in a program.)
# #two main types.
# # 01_local scope : created and used only inside a function.

def greet():
    name = "sara"        #works inside function.
    print(name)
greet()
#print(name)         #error: doesn't work

#global scope:
country = "pakistan"           #outside 
def show_country():
    print(country)        # works inside a function
show_country()

print(country)          # works outside as well


#default parameter:
def greet(name = "ahmed"):       #default value : works when arguments aren't given
    print(f"hello",(name))
greet()                #arguments aren't given.


#practice task:              An online shopping app:
def shopping(product, quantity = 1):
    print(f"prouct :",(product))
    print(f"quantity:", (quantity))
shopping("laptop", 3) 


#student information:
def student():
    name = "darakhshan"
    age = 17
    department = "BSCS"
    print(f"students name :",(name))
    print(f"age :",(age))
    print(f"department :",(department))

student()

#employee data:
def employee(name = "zorab", age = 23 , post = "teacher"):
    name = "ali"
    age = 25
    post = "Junior Software Enginner"
    print(f"hello", (name))
    print(f"we like to hire you as", (post))

employee()

 

#week  : 03                   Day : 06
 #*args (variable positional arguments)
# It is used to pass many arguments to a function.

def numbers(a,b,c,d):
    print(numbers)
numbers(3,5,6,7)                  

def numbers(*args):
    print(args)
numbers(5,7,2,4)          #call function 

def names(*args):
    print(args)
names("ali",45.3,"haider")

#through loop:
def show(*args):
    for number in args:
        print(number)
show(9,3,2,1,4)
show("sara","zara","noor","taha")

#shopping cart:
print(f"""=====
Shopping list
======
""")
def shop(*args):
    for item in args:
        print(item)
shop("milk","eggs","bread","honey","sugar","oil")



#   **kwargs:   variable keyword arguments:
# with in help of **kwargs , we can pass a key_value data to a function in arguments.
def data(**kwargs):
    print(kwargs)
data(name = "hashim", age = "21" , post = "junior clerk")
  # **kwargs stores this values as dictionary.



#loop through **kwargs:
def information(**kwargs):
    for key , value in kwargs.items():
        print((key),":",(value))
information(name = "sara", qualification = "graduated", post = "junior employee", salary = 45000 )




#Recursion: means a function call itself.
def call_it(n):          # function definition
    if n == 0:            #  base_condition
        print("done")
    else:
        print(n)
        call_it(n - 1)           #funtion calls itself.
call_it(6)          




#practice task:

#print all numbers:
def show_numbers(*args):
    print(args)
show_numbers(1,2,3,4,5,6,7,8,9,0)

#sum using *args
def sum(*args):            #args method in function.
    args = 9 +5 +6 +2         # these numbeers are pass to function as tuple.
    print(args)
sum()                      #function call

#user profile:
def profile(**kwargs):
    for key , value in kwargs.items():
        print((key),":",(value))
   
profile(name = "wahab", user_name = "Wahab34#0", email = "wahab000@gmail.com", interest = "contant creation")

#countdown:
def count(n):
    if n == 0 :
        print("time over")
    else:
        print(n)
        count(n-1)
count(10)


