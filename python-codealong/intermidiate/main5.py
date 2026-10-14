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
b = [i*i for i in mylist]

print(mylist)
print(b)
