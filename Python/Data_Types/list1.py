name=['raj','kabir','anuj','harsh','soham']
print("The intitial list is :")
print(name)
print(name[3])

#multidimentional list
names=[['raj','soham'],['anuj','kabir']]
print(names[0][1])
print(names[1][1])

#print using or loop
print("\nPrinting of list using for loop")
for i in name:
    print(i)

#-ve Traversing
print("\n-ve Traversing")
print(name[-1])
print(name[::-1])

#split
string = ("Rajvardhan Gajanan Ulape")
l1=string.split()
print("The list is ",l1)

#append
name.append("Ruturaj")
#name.extend(3)
print(name)

#insert
name.insert(3,'sonya')
print(name)