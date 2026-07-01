#week 02 : Day 01:
#strings [text in pyhton]
#string : sequence of characters.
name = "ahmed"       # value closed in double quotes
caste = 'shaikh'     # in single quotes

#indexing:       used to access any character from sequence.
city_name = "Hydrabad"
print(city_name[5])       #output : b

#negative indexing : 
city_name = "Hydrabad"
print(city_name[-5])     #output : r

#slicing : to print specific characters of string.
course = "python"
print(course[2 : 5])   # output : tho 

print(course[:4])      #auto start from index 0 
                       #output : pyth

#negative slicing : 
print(course[:-3])      #output : pyt


#convert string into uppercase :
greeting = "good morning!"
print(greeting.upper())

#convert string into lowercase :
greeting = "GOOD EVENING!"
print(greeting.lower())


#remove spaces: keyword(strip)
text = "    welcome  to  Dubai    "   # remove spaces from the beginning and end of a string.
print(text.strip())


a = "  bravo  "        # output : bravo included spaces.
print(a)

print(a.strip())     #only bravo not spaces.and


#replace text :
new = " hello ! welcom to java course."
print(new.replace("java", "pyhton"))    # output : java converted into pyhton .


#find length :
print(len(new))    # variable (new) carry 31 characters.


title = "weak hero"
print(len(title))     # length is 9 included space.

greet = "welcome to our website"
print(greet[0])                  #first character of the string.

print(greet[21])                 #last character of the string.






