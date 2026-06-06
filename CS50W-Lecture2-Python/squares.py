#to import values from anotehr document o file
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")

# you can use this another way to import values from anotehr document o file
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")