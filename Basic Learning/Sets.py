# #Sets
 collection = {1,2,3,3,2,2,"hello", "kunj","world",4}
# print(collection)
# print(type(collection))
# print(len(collection))

# null_set = {} #it is to empty dict not set
# print(type(null_set))
# coll = set()  #add parenthesis
# print(type(coll))

#Set methods

#set are mutable but set elements are immutable
set1 = {2,4,5,6,7,4,53,5,5,3,34}
set1.add(10)
print(set1) #lists add na thay, unhashable
set1.remove(53)
print(set1) #if value is not present in set than it will throw erre
# print(set1.clear())
# print(set1.pop()) #random removal


print(set1.union(collection))
print(set1.difference(collection))