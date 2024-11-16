thisset = {"raj","kabir","anuj","rohit","pranav","aniket","samix", True , 1,2}
print(thisset)

#length
print(len(thisset))

#type
print(type(thisset))

# set creation using set constructor
set = set(("apple","banana","cheery"))
print(set)

#Access set items
for x in thisset:
    print(x)

print("banana"in set)

#update set
set.add("orange")
print(set)

#update using update method 
tropical = {"soham",1,3,3.25,"mayank"}

set.update(tropical)

print(set)

#remove
thisset.remove("samix")
print(thisset)

#pop
x= thisset.pop()
print(x)
print(thisset)

#clear function
thisset.clear()
print(thisset)