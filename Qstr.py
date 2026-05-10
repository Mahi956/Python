# -------STRING-------

# Name = "Mahi_Sharma"
# Fruit = "Mango"
# print(Name)
# print(len(Name))
# print(len(Fruit))
# print(Name[0:2])
# print(Name[2:3])
# print(Name[2])
# print(Name[:3]) # by default it's [0:3]

# print(Name[:-5])
# print(Name[0:len(Name)-5]) 
# print(Name[0:len(Name)-3]) 
# print(Fruit[0:len(Fruit)-3]) 

# **************************************************************

# Strings are immutable 

a = "mahi"
print(a)
# print(len(a))
# print(a.replace ("mahi" , "Max"))
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
print(a.rstrip("i"))

b = "hey_you_guys_wadup"
print(b.split("_"))
print(len(b.center(50)))
print(len(b))
print(b.count("y"))
print(b.endswith("ls"))