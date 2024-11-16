str="RajvardhanGajananUlape"
print("The initial string : ")
print(str)

# traversing with +ve index
print(str[5])
print(str[2:10])
print(str[10:17])

# traversing with +ve index
print(str[-5])
print(str[-5:-1])
print(str[::-1])

# length
print(len(str))

#reverse and join
reverse="".join((reversed(str)))
print(reverse)

#update
str1=(str[0:10]+"_"+str[10:17]+"_"+str[17:])
print(str1)