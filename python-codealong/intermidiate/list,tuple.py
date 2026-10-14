#lists : orded mutable allows dupes
mylist = ["banana", "cherry", "apple"]
print(mylist)
if "banana" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.insert(1, "blueberry")
print(mylist)

mylist.pop()
print(mylist)

a = [1,2,3,4,5,6]
b = [i+i for i in mylist] #retuns square give an expression then apply a for loop

print(mylist)
print(b)



#tuples
mytuple = tuple(["Max" , 28, "boston"])
print(mytuple)

if "boston" in mytuple:
    print("yes")
else:
    print("no")
