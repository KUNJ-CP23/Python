#lists allows to store multiple type data in single list
marks = [94.5, 99.4,97.6,96.7,99.7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
[print(len(marks))]

#lists are mutable
student = [ "Kunj" , 9.8 , 3 , "Rajkot"]
print(student)
student[3] = "Earth"
print(student)

#lists slicing
#(ending index not included)

print(marks[1:4])
print(marks[0:])
print(marks[:3])
print(marks[-5:-1])
print(marks[:-3])

