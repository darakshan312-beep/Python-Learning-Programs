#week 02: day 04:
#list : collection of multiple items stored in a single variable.
#list[]

glosary = ["rice", "oil", "milk", "bread"]
print(glosary) 

students = ["Ahmed", "Sara","Faiza"]
print(students)

#Access list items: by indexing number.
print(students[2])
print(glosary[0])

#Negative indexing: 
print(students[-2])     

#changing items : because lists srre mutable so we can change it after creation.
days = ["monday","wednesday","thursday", "friday","saturday","sunday"]
days[1] = "tuesday"
print(days)            #tuesday comes at the place of wednesday.

#Add items:   use append() keyword.
num = [1,2,3,4,5]
num.append(6)
print(num)
print(len(num))

#Removing items.
num.remove(4)
print(num)

#length of list:
print(len(num))

#loop through a list:
for number in num:
    print(number)      # print each number from the list one by one.

for number in num:
    print(num)        #print whole list 5 times because list contain 5 values.

names = ["zoya", "saira","Ahmer"]
for my_name in names:
    print(my_name)      



#practice Task:
favorite_sub = ["english", "maths","physics","chemistry"]
print(f""" ======
my favorite
subject is=====
""")
print(favorite_sub[2])


#shopping list:
shopping = ["milk","teapack","fries"]
shopping.append("juice") 
print(shopping)


#remove milk:
shopping.remove("milk")
print(shopping)


#student list:
student = ["ali","zoya","jerry","talha"]
for students in student:
    print(students)