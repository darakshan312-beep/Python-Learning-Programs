#day 05 of python programming practice .
#loop concept : loop is used to run a block od code multiple times.

#for loop

for i in range(10):     #in this i value from 0 (by default) to 10 will print with the help of for loop.
     print(i)


for a in range(1,10):   #custom range.
     print(a)

#while loop

count = 1                #create a variable.
while count <= 5:       #set its condition 
     print(count)         #instruction 
     count += 1


count = 5                #start from this 
while count > 0:         # till this value (>) sign used for moving forword.
     print(count)       
     count -= 1           # how will this loop works . (in decrement form).

print("go!") 


# #practuice task 
# #display numbers from 0 to 10
for i in range(11):
     print(i)


name = ("carry")
while name >= 5:
     print(name)

#while loop
count = 5
while count > 0:
    print(count)
    count -= 1


num = 10
while num < 15:
    print(num)
    num += 1 

for a in range(5):
    print("darakhshan")     #to print any string in loop.

for i in range(5):         #to print any integer value in loop.a
    print(i)

#practice task 
# countdown:
for i in range(5):
    print(i)

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1 
print("start")


#display numbers from 1 to 10:
for i in range(1 , 11):
    print(i)

#print your name 5 times:
for name in range(5):
    print("Darakhshan")    


#multiplication table of two:
for t in range(1 , 11):
    print(" 2 x", t ,"=",2*t)


#table of 5:
for f in range(1 , 11):
    print("5 x", f ,"=" , 5*f)




p = int(input("enter any number:"))
for t in range(1 , 11):
     print(p, " X " ,t, "=", p * t)


#how to use break:
for b in range(1 , 11):
    if b == 5:
        break 
    print(b)




#nested loop = loop inside another loop.
for i in range(5):
    for j in range(3):
        print(i ,j)
