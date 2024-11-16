#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set5 ={"soham","raj","sai","Aarush"}

set3 = set1.union(set2)
print(set3)

# union using sign |
set = set1 | set5

print(set)
#intersection 
set4={"raj","kabir","anuj"}

set6 = set4.intersection(set5)
print(set6)

#intersection using symbol

setx = set4 & set5
print(setx)

# set difference
seta = {"apple", "banana", "cherry"}
setb = {"google", "microsoft", "apple"}

setc = seta.difference(setb)

print(setc)