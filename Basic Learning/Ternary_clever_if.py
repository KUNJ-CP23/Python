#single line if / ternary operator

football = input("football : ")
goal = "did it" if football=="goes into post" else "missed it"
print(goal)

# ternary 2
food = input(str("food : "))
print("sweet") if food == "cake" or food == "pastry" else print("not sweet")

# clever if  (false,true)
age = int(input("age : "))
vote = ("yes", "no") [age < 18]
print(vote)