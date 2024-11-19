#Dictionary methods

info = {
    "name" : "Kunj",
    "subjects" : ["c", "java", "js","python"],
    "topic" : ("dictionary","sets"),
    "face" : "beautiful",
    "age" : 19,
    "is_adult" : True,
    23.3 : 323
}
print(info.keys())
student = {
    "name" : "Kunj",
    "subjects" : {
        "phy" : 99,
        "math" : 100,
        "chem" : 100
    }
}
print(student.keys()) #does not print nested keys

#type casting as list
print(list(student.keys()))

#total keys
print(len(student.keys()))

#values
print(list(info.values()))

#returns pair
print(list(info.items()))
pairs = list(student.items())
print(pairs[0])

#get(why needed, answered below)
print(student["name"])
print(student.get("name"))
#ps name2 dont exist
#(student["name2"]) #error, not prefferes as code after this does not get executed
print(student.get("name2")) #no error -> None

#update
student.update({"city" : "rajkot"},{"age" : 19}) #if same named key is added then value is overwritten
print(student)

#pop
print(student.pop("name"))
