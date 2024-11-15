#conditional statement --> is-elif-else

light = input("light color : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else: 
    print("light is broken")

# eg 2

marks = int(input("marks : "))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks <90):
    print("B")
elif(marks >= 70 and marks <80):
    print("C")
else:
    print("D")

#nesting conditional
age = 95
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
