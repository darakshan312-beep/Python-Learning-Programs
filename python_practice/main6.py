#week 02: day 03:
#string formatting and escape characters.
#recommended method ( f-strings )

#f_strings:
name = "ahmed"
age = 28
print(f"my name is {name} ")    #f tells ,replace anything inside{} with its value.


#escape characters:  used for special formating.
#new line ( \n ):
print("hello\nTrainee")

#tab space (\t):
print("darakhshan\t18 years old ")

#quotes inside string (\"    \"):
print("he said\"hello\"") 

#backslash (\ \):
email = ("c: \\user\\@gmail.com")
print(email)

#multi-line strings ( """     """):
print("""
good 
morning
pakistan
""")

#text alignment:

name = "Zohaib"
print(f"{name:<50}")    #left align:
print(f"{name:>50}")    #right align:
print(f"{name:^50}")     #center align:

#practice task:
                     #Student Card

card = "student card"

print(card.center(50))
name = "carry holy"
roll_no = 2025 
depart = "BSCS"


print(f"""
===== STUDENT CARD =====
Name : {name}
Roll no : {roll_no}
Department : {depart}
==============
""")


#personal info:
name = " mohib ali"
age =  24
qualification = "teacher"
print(f"hey {name}")
print(f"your age is \n{age} ")
print(f"you are a {qualification}")
print(f"you are eligible for \nthis loan ")


#multi_line quotes:
she = "I am nervous"
he = "but why"
father = "its her first day of the job"

print(f"""
she said : {she}
he said in wonder : {he}
father explain him : {father}
""")
