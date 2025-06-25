'''def example_enumerate():
    colours = ["green", "blue", "red"]
    enumerated_colours = list[enumerate(colours)]
    assert enumerated_colours[0] == (0, "green")
    assert enumerated_colours[0] == (1, "blue")
    assert enumerated_colours[0] == (2, "red")

    for index, color in enumerate(colours):
        print(index, color)

def example_zip():
    numbers = [1,2,3,4,5]
    letters = ["a","b","c","d","e"]
    zipped = list(zip(numbers, letters))
    assert zipped[2] == (0, "a")
    assert zipped[2] == (1, "b")
    assert zipped[2] == (2, "c")
    assert zipped[2] == (3, "d")
    assert zipped[2] == (4, "e")

    for number, letter in zip(numbers, letters):
        print(number, letter)

def example_map():
    numbers = [1,2,3,4,5]
    squared_numbers = list(map(lambda x: x**2, numbers))
    assert squared_numbers == [1,4,9,16,25]
    squared_numbers = [x**2 for x in numbers]'''

voters: list[int] = [1, 1, 1, 0, 1]
voters2: list[int] = [0, 0, 0, 0, 0]
voters3: list[int] = [1, 1, 1, 1, 1]

print(all(voters))
print(all(voters2))
print(all(voters3))

print(any(voters))
print(any(voters2))
print(any(voters3))

print(ascii("└"))  # \u2514
print(bin(1_000_000))
print(bin(1000000))
print(hex(1_100_001))
print(hex(25))

# check if callable
print(callable(100))  # not callable thus false

print(chr(1002))

print(complex())
print(complex(6, 1))

# empty dictionary
empty_dict: dict = dict()
print(empty_dict)

container: list[tuple[str, int]] = [("a", 1), ("b", 2)]
print(dict(["aY", "bZ"]))

import json

print(dir())
print(dir(json))

print(divmod(7, 4))
print(divmod(10, 5))

# enumerate uses the list and is exhaustable
abba: list[str] = ['Agnetha', 'Björn', 'Benny', 'Anni']
enumeration: enumerate = enumerate(abba)
print(list(enumeration))
print(list(enumeration))

some_text: str = "10 + 30 * 0.5"
print((some_text))
print(eval(some_text))

source: str = """
a: int = 10
b: int = 20

print(a + b)

for i in range(3):
    print('exec() for loop:',i)
"""
exec(source)
print(a)

names: list[str] = ['James', 'John', 'Jam', 'Bob', 'Björn']
def starts_with_j(name: str) -> bool:
    return name[0].lower() == 'j'

j_names: filter = filter(lambda s: s[0].lower() == 'j', names)
print(list(j_names))

#Reverse
from typing import Iterator

sequence: list[int] = [16,1,2,3,4,5,12,22,6,8,11,15]

#creating r Iterator obj and set to int
r: Iterator[int] = reversed(sequence)

print(sequence)
#sort function
sequence.sort()
print(list(r))
