try:
    a = 5 / 0
except:
    print('some error occured.') # prints this if something goes wrong

try:
    a = 5 / 0
except Exception as e:
    print(e) # prints what the error actually is

try:
    a = 5 / 0
except ZeroDivisionError:
    print('Only a ZeroDivisionError is handled here') # runs only if we divide by zero

try:
    a = 5 / 1 
    b = a + '10' # cant add a number and a string
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e) # runs if we divide by zero
except TypeError as e:
    print('A TypeError occured:', e) # runs if the data types dont match




try:
    a = 5 / 1 
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)
else:
    print('Everything is ok')
finally:
    print('Cleaning up some stuff...')




class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(a):
    if a > 1000:
        raise ValueTooHighError('Value is too high.')
    if a < 5:
        raise ValueTooLowError('Value is too low.', a) 
    return a

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, 'The value is:', e.value)



# logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info('HELLO')

class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

stream_handler = logging.StreamHandler()
stream_handler.addFilter(InfoFilter())
logger.addHandler(stream_handler)

# json
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

print(person_json)
print(person_json2)

person_json = """
{
    "age": 30,
    "city": "New York",
    "hasChildren": false,
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person = json.loads(person_json)
print(person)

zJSON = """
{
    "complex": {
        "real": 3,
        "imag": 4
    }
}
"""

z = json.loads(zJSON)
print(type(z))
print(z)

def decode_complex(dct):
    if "complex" in dct:
        return complex(dct["complex"]["real"], dct["complex"]["imag"])
    return dct

z = json.loads(zJSON, object_hook=decode_complex)
print(type(z))
print(z)
z = json.loads(zJSON, object_hook=decode_complex)
print(type(z))
print(z)

