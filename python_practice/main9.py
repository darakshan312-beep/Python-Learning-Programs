#week : 03                         day : 01
#tuples : A tuple is a collection of multiple items, just like a list. (immutable)

days = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days)
#lets try to make change in it.
# days[1] = "sunday"
# print(days)                        #error 

colors = ("red","yellow","blue","white")
#length
print(len(colors))    
#access through indexing:
print(colors[2])
#-ve indexing:
print(colors[-1])


#loop through a tuple:
for color in colors:               #access elements of tuple one by one.
    print(color)

#check if an item exists ?
print("blue" in colors)

#converting list into tuple:
items = [1,2,3,4,5]
items = tuple(items)      
print(items)       
# #changing: 
# items[3] = 7                         #error
# print(items)

#converting tuple into list:
row = (2,4,6,8)
row = list(row)
row[3] = 7
print(row)             #output changed because this tuple is now a list which can be changed.

#practice task:
countries = ("pakistan","india","iran","china")
#print all countries:
print(countries)        #01 method            #output in 1 line.

for country in countries:
    print(country)             #02 through loop            #output = print each country one by one

#first country:
print(countries[0])             
#last country:
print(countries[3])

#length:
print(len(countries))

#exists ?
print("iran" in countries)





#week : 03                            day :02
#Dictionary:     A dictionary stores data in key_value pairs.

#why is used:  because it is clear and easy to understand.

student = {

    "name" : "darakhshan",
    "age" : 18,
    "course" : "python"
}
print(student)

car = {
    "name" : "toyota",
    "model" : 2025,
    "price" : 12000000 ,
}
print(car)

#access value:
print(student["name"])        #method_01

print(student.get("course"))      #method_02 : through get() method.

#if key doesn't exist : output none.
print(student.get("caste"))

#changing value:         
student["age"] = 20
print(student)

#adding new data:         #dictionary[]
student["grade"] = "A"
print(student)

#removing data:           #pop()
student.pop("course")
print(student)

#lenght :
print(len(student))       #len()


#check if exist:
print("name" in student)     #in

#loop though dictionary:
for key , value in student.items():          # .items()
    print(key ,":" , value) 

#practice task:
#employee data:

print(f"""
======
employee file
======
""")
employee = {
    "name":"Ahmed",
    "age": 23,
    "qualification": "graduated",
    "internship" : "true",
    "experience": "2 years" ,
    "salary" : 75000
}

for key , value in employee.items():
    print(key, ":" , value) 

# print(employee["graduated"])               #error : dictionary[key] not [value]

employee["performance"] = "Good"
print(employee)

employee.pop("internship")
print(employee)



#week : 03                Day : 03
#sets : A set is a collection of unique items.              no duplicates , unordered
numbers = {1,2,3,3,4,5,6,2}
print(numbers)

alphabets = {"A","B","C","D","B","c"}                   
print(alphabets)

#adding item:
numbers.add(7)
print(numbers)

alphabets.add("G")
print(alphabets)

# Set Operations
a = {"taha","rauf","urwa"}
b = {"rauf","abdul","saif"}
print(a | b)                     #union : combine all sets. 
print(a & b)                     #intersection : common element in both sets.
print(a - b)                     #difference : find the unique elements in first set but not the second.


#removing item:
print(a.remove("taha"))

#check if item exist:
print("rauf" in a)

print(len(b))
