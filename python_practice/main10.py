#week : 03                  Day : 04
#function = A function is a reuseable block of code that performs a specific task.
#it is used to separate code .

def greet():
    print("hello")            #create a funtion

greet()                   #call it.

def greet(name):
    print(f"hello",(name))
greet("ali")
greet("sara")
greet("ahmed")


def age(a):
    print(f"your age is",(a),"years")
age(17)


def calculate(a,b):         #function
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
calculate(9 , 4)           #call
calculate(2 , 4)

def add(a,b):       #create a function 
    return a+b         #return back its value
y = add(3,2)     # y variable will store retruned value.
print(y)


print(y*y)


#practice task:
#personalize greeting.
name = input("enter your name :")        #greeting function
def greet(name):
    print(f"hello",(name))
greet(name)

#add two numbers.
def add(x,y):
    return x + y
result = add(3 , 5)
print(result)

#square of number.
a = int(input("enter a number:"))            #ask user to input
def square(a):                               #function
    return a*a                               #retrun value
result = square(a)                           #stores returned value
print(result)                                #display

#parameters : the variable names listed in a function,s definition.
#arguments : the actual value passed to the function when you call it.






#week : 03                        day : 05
#how to pass arguments to functions.

def average(a,b):       #required arguments.
    print("the average is ", + (a+b)/2)
average(8,2)

#types of aruguments that can be provide in a function:
#default argument
#keyword arggument
#variable length argument
#required argument


def average(a=4,b=3):       #default argument
    print("the average is ", + (a+b)/2)
average()
average(5)       #one value will function get by default.
average(8,9)     #this given will be consider main arguments and 

#keyword arguments : provide argument with key= value , order does not matter.
average(b=5, a=3)  

#variable_length arguments:
def average(*numbers):  #iterate numbers : As tuple: store as much numbers as you can.
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        print("the average is", sum / len(numbers))
average(5,6,7,8)                   #lenth of arguments can be increase or decrease.


def name(**name):
    print(type(name))       #as dictionary : because it stores key_value type data.
    print("hello,",name["fname"], name["mname"], name["lname"])

name(mname = "halk" , lname= "gamma", fname = "ellas") 