str = "this is a coder girl you all"

print(str.endswith("ll"))
str = str.capitalize()
print(str) #prints only one time as string is immutable
print(str.replace("a" , "k"))
print(str.replace("coder","coding"))

print(str.find("k"))
print(str.find("coder"))
print(str.find("a"))

print(str.count("a"))

print(str.center(5))
print(str.isalpha())
print(str.isdigit())
print(str.isnumeric())
print(str.istitle())
# there are more methods like rstrip, lstrip, rjust, ljust and many more
