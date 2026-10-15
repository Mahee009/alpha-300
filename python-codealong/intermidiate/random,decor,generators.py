#random example 1
import random

# random floats
a = random.random()
print(a)

a = random.uniform(1,10)
print(a)

# random integers
a = random.randint(1,10)
print(a)

a = random.randrange(1,10)
print(a)

a = random.normalvariate(0, 1)
print(a)

# random selection
a = random.choice(list("ABCDEFGHI"))
print(a)

a = random.sample(list("ABCDEFGHI"), 3)
print(a)

a = random.choices(list("ABCDEFGHI"),k=3)
print(a)

a = list("ABCDEFGHI")
random.shuffle(a)
print(a)


#exp 2 
print('Seeding with 1...\n')

random.seed(1)
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 1...\n')
random.seed(1)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))


#decorators


def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')

print_name() # calls the function normally

print()


def start_end_decorator_2(func):

    def wrapper(*args, **kwargs): # accepts any number of arguments
        print('Start')
        func(*args, **kwargs) # calls the original function
        print('End')
    return wrapper

@start_end_decorator_2 # wraps the function with extra code
def add_5(x):
    return x + 5

result = add_5(10)
print(result)


import functools

def start_end_decorator_4(func):

    @functools.wraps(func) # preserves the original function's info
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs) # stores the returned value
        print('End')
        return result # returns the result to the caller
    return wrapper

@start_end_decorator_4
def add_5(x):
    return x + 5

result = add_5(10)
print(result)
print(add_5.__name__) # prints the original function name
help(add_5) # shows the function's documentation




#generators 
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(3)#not print 'Starting'


print(next(cd)) # print 'Starting' and the first value


print(next(cd))# print the next values
print(next(cd))


print(next(cd))# this will raise a StopIteration


def fibonacci(limit):
    a, b = 0, 1 # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
print(list(fib))


class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()

firstn_object = firstn(1000000)
print(sum(firstn_object))




