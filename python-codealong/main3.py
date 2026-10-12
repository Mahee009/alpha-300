def change(value):
    value = 2
val  = 1 #immuatable
change(val)
print(val) #prints 1 because the value of val is not changed in the function change




def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ') 
    for word in words:
        say(word)

talk('I am going to buy the milk')


def counter():
    count = 0

    def increment(): 
        nonlocal count #used bcoz count is not defined and we cannot use a local function or take it from counter so we use non local 
        count = count + 1
        return count
    return increment 
increment = counter()

print(increment()) #1
print(increment())#2
print(increment())#3


age = 4

print(age.real)
print(age.imag)
print(age.bit_length())


items = [1,2]
items.append(3)
items.pop()
print(id(items)) #prints the id of the obj

#loops
for item in enumerate(items): #each item and idex of item
    print(item)


#classes
class animal:
    def walk(self):
        print("walking...")

class dog(animal): #dog is inheriting the properties of an anumal class
    def __init__(self, name, age):# to initiaze one more properties when we create a class a new obj from that class we use init method and self is used to point to the current obj instance
        self.name = name
        self.age = age
    def bark(self): #will point to a current obj instance and must be specified when defining a method 
        print("woof")

roger = dog("roger", 8)

print(roger.name)
print(roger.age)
roger.bark()


#Recursion 
def factorial(n):
    if n == 1 : return 1 # base case
    return n * factorial(n-1) # recursive 

print(factorial(3))
print(factorial(4))
print(factorial(5))

# exceptions 
# try:
#some line sof cocde
#except <ERROR1>:
#some line sof cocde
#except <ERROR2>:
#else: no expectiosn rraised
#finally: will always run no matter what

#polymorphism
class dog:
    def eat(self):
        print("eating...")