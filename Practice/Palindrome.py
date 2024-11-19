
list1 = [1,2,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("it's a palindrome")
else:
    print("not palindrome")

print(list1.count(1))
list1.sort()
print(list1)