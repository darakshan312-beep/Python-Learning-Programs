#week 02:  Day 02
#string methods: used to handle and ajdust string according to our need.

name = "awais arhsad"
print(name.capitalize())    #only capitalize the first letter of the string.

city = "    hydrabad   "
print(city.strip())         #remove spaces from start and end.

address = "talib ul mola colony"
print(address.split())               #separate each word.


new = "darakhshan"
print(new.count("a"))              #count occurance of letter a in a string.
print(new.split())
print(new.center(150))               #it makes given string of 150 characters by adding spaces into it .

a = "hye", "my", "name", "is" ,"john"
sentence = " ".join(a)
print(sentence)                      #joins a strings.


s = "user@gmail.com"
print(s.startswith("user"))            #output : ture
print(s.endswith("gol"))                 #output : false (because s not endswith gol)




#practice task: create a username cleaner.
name = input("enter your name:")
print(name.strip())
print(name.upper())
print(name)