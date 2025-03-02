import time

def power(limit):
    return [x**2 for x in range(limit)]
start = time.time()
power(5000000)
end = time.time()
print(end-start)

import timeit
print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))

#The time module provides functions for working with dates and times in Python.
#The time module has a function called time() that returns the current time in seconds since the epoch.
#The time module has a function called sleep() that pauses the program for a specified number of seconds.
#The time module has a function called strftime() that converts a time object to a string.


