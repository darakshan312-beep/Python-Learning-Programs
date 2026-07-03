#day :5 , week : 02
#advanced list 

students = ["ali","sara","ahmed","zora","shazaib"]
print(len(students))

#insert
students.insert(2,"faiza")      #through insert method , we can add an iten in list along with its index number
print(students)
print(len(students))

#pop()
removed = students.pop(3)
print(removed)
print(students)

new = [45,"name",90,"alai",True]    #multi datatype list
remove = new.pop(2)
print(remove)
print(new)

new.pop()    # last element removed
print(new)


#check if an item exist:
girls_name = ["sara","urwa","shifa","ansha","tahreem"]
print("sara" in girls_name)
print("zoya" in girls_name)   #output : boolean value 


#find an item's position:
print(girls_name.index("tahreem"))

#sorting list:
numbers = [20,76,94,13,63,78,23]
numbers.sort()
print(numbers)

#sorting alphabets:
fruits = ["banana","apple","orange","graphs","papaya","cherry"]
fruits.sort()
print(fruits)

#reverse a list:
numbers.reverse()
print(numbers)

#copy a list:
new_fruits = fruits.copy()
print(new_fruits)

#slicing list:
print(fruits[1:3])

items = ["milk","sugar","floar","teapack","rice"]
print(items[0:3])

#loop with index:
for index, item in enumerate(items):     #enumerate : get both index and value while looping.
    print(index, item)


#real_life example :
students = ["azhar","raza","ahsan"]
for number , student in enumerate(students , start = 1):
    print(f"{number}.{student}")




#practice task:
#mini student manager.

#add 5 students name:
students =[]
students = ["farwa","haya","hoorain"]    #1 method
students.append("ali")                    #2 method
students.append("sara")
students.append("falak")
students.append("dua")
students.append("taha")
print(students)

students.insert(5,"zain")           #3 method
print(students)

#sort names alphabetically:
students.sort()
print(students)


print(f""" ======
attendence list of students
    ======""")

#print numbered list:
for number, students in enumerate(students , start = 1):
    print(f"{number}.{students}")

#ask the user for a student name and check:
st  = ["naila","haider","farook"]
name = input("enter student name: ")
if name in st:
    print("student found")
else:
    print("student not found")