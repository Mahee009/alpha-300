mydict = {"name": "Max", "age": 28, "city": "NY"}
print(mydict)

value = mydict["age"] #can be replaced with age, name, city depending on requirement 
print(value) #if unvalif valur keyerror

mydict["email"] = "xyq@ff.com"
print(mydict)
 # del mydict["name"], mydict.pop("age")
#print(mydict)

try:
    print(mydict["name"]) #to check if the variable name exists if not rfeturn error
except:
    print("error")

for value in mydict.values():
    print(value) #prints all the values in the dict

my_dict = {"name": "marry", "age": 20, "email": "scy@jj.com"}
my_dict2 = dict(name="marry", age=20, city="ny" )

my_dict.update(my_dict2)# takes value from new dic and adds to old one 
print(my_dict)


#set
myset = {1, 2, 3, 4} 
#no duplicates allowed, its a good method to find out how mnay eelments present 
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.discard(2)
print(myset)

odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(even)
print(u)

i = odds.intersection(primes)
print(i)
#setA.diffrence_update(setB) updates setA as the diffrence of a and b 

#string
my_string = 'jow,are,you'
my_list = my_string.split()
print(my_list)
new_string = ' '.join(my_list)
print(new_string)
