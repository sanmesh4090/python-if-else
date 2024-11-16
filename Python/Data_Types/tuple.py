thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#length
print(len(thistuple))

#Type 
print(type(thistuple))

#creation of tuple by using tuple constructor
#tuple with diffrent datatypes
tuple = tuple((17,"raj",12.5, True))
print(tuple)

#indexing 
print(thistuple[2])

#negative indexing
print(tuple[-1])

#accesing data using range
print(tuple[2:4])

print(tuple[:4])

#update tuple
y = list(thistuple)
y.append("orange")
print(y)

z=("kiwi",)
thistuple += z
print(thistuple)

#delete
y.remove("apple")
print(y)

del(thistuple)
print(thistuple)