from collections import Counter #counter stores the elsments in their fictional keys 
a = "aaaaaaaaaaabbbcccc"
my_counter = Counter(a)
print(my_counter.keys)
print(my_counter.values())

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

print(my_counter.most_common(1))#common items

print(list(my_counter.elements())) # Return an iterator over elements repeating each as many times as its count
# Elements are returned in arbitrary order

from collections import namedtuple# create a namedtuple with its class name and its fields as string
# fields have to be separated by comma or space in the given string

Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y)

Person = namedtuple('Person','name, age')
friend = Person(name='Tom', age=25)
print(friend.name, friend.age)

from collections import defaultdict# initialize with a default integer value,0
d = defaultdict(int)
d['yellow'] = 1
d['blue'] = 2
print(d.items())
print(d['green'])# initialize with a default list value,an empty list
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    d[k].append(v)

print(d.items())
print(d['green'])

from collections import deque
d = deque()

# append() : add elements to the right end 
d.append('a')
d.append('b')
print(d)

# appendleft() : add elements to the left end 
d.appendleft('c')
print(d)

# pop() : return and remove elements from the right
print(d.pop())
print(d)

# popleft() : return and remove elements from the left
print(d.popleft())
print(d)

# clear() : remove all elements
d.clear()
print(d)

d = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j']) # 'j' isat the left most position
print(d)

# count(x) : returns the number of found elements
print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)

#intertools
from itertools import product

prod = product([1, 2], [3, 4])
print(list(prod)) #convert the iterator to a list for printing


prod = product([1, 2], [3], repeat=2) # to allow the product of an iterable with itself specify the number of repetitions 
print(list(prod)) # e convert the iterator to a list for printing


from itertools import accumulate


acc = accumulate([1,2,3,4])# return accumulated sums
print(list(acc))


import operator# other possible functions are possible
acc = accumulate([1,2,3,4], func=operator.mul)
print(list(acc))

acc = accumulate([1,5,2,6,3,4], func=max)
print(list(acc))


from itertools import groupby


def smaller_than_3(x):
    return x < 3

group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))

group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))


    #lamda 

    
f = lambda x: x+10 # adds 10 to the input argument
val1 = f(5)
val2 = f(100)
print(val1, val2)


f = lambda x,y: x*y # multiplies two input arguments and returns the result
val3 = f(2,10)
val4 = f(7,5)
print(val3, val4)


def myfunc(n):
    return lambda x: x * n

doubler = myfunc(2)
print(doubler(6))

tripler = myfunc(3)
print(tripler(6))


from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)


a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x%2 == 0) , a))


c = [x for x in a if x%2 == 0]
print(b)
print(c)


a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))
c = [x*2 for x in a]
print(b)
print(c)
