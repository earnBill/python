#import a function from another file (functions.py) 
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")