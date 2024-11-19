#dictionary --> unordered and mutable
#lists and dict are mutable but tuple is not hence it can be used as key 
info = {
    "name" : "Kunj",
    "subjects" : ["c", "java", "js","python"],
    "topic" : ("dictionary","sets"),
    "face" : "beautiful",
    "age" : 19,
    "is_adult" : True,
    23.3 : 323
}

print(info)
print(type(info))
print(info["name"])

info["age"] = 20 #overwrites
info["lastname"] = "Ramoliya"
print(info)

null_dict = {}

#nested dictionary
student = {
    "name" : "Kunj",
    "subjects" : {
        "phy" : 99,
        "math" : 100,
        "chem" : 100
    }
}

print(student["subjects"]["phy"])
