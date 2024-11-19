tup = (1,4,6,66,6,6,3,7,9)
print(type(tup))
print(tup[0])
print(tup[1])

tup1 = ()
print(tup1) 
print(type(tup1))

#tup1 = (1) is taken as integers

tup2 = (1,)
print(tup2)
print(type(tup2))

#slicing here is same as lists
print(tup[1:3])

#methods
print(tup.index(3))
print(tup.count(6))