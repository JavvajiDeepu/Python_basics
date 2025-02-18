from collections import Counter
device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

#print(Counter({'Hello': 5, 'World': 5})['World'])#TypeError: 'type' object is not subscriptable

#The Counter class is a subclass of the dictionary class. It is used to count the frequency of elements in a list.
#The Counter class takes an iterable as an argument and returns a dictionary with the elements of the iterable as keys and their frequency as values.
#The Counter class has a method called most_common() that returns a list of tuples containing the elements and their frequency, sorted in descending order of frequency.

####deaultdict####
#The defaultdict class is a subclass of the dictionary class. It is used to create dictionaries with default values for keys that do not exist.
#The defaultdict class takes a function as an argument that returns the default value for keys that do not exist.
#The defaultdict class has a method called default_factory that returns the default value for keys that do not exist.
from collections import defaultdict
Coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]
alma_maters = defaultdict(list)
for coworker, place in Coworkers:
    alma_maters[coworker].append(place)
print(alma_maters)

###namedtuple###
#The namedtuple class is a factory function that returns a tuple subclass with named fields.
#The namedtuple class takes two arguments: the name of the tuple subclass and a list of field names.
#The namedtuple class has a method called _make() that creates a new instance of the namedtuple subclass from an iterable.


from collections import namedtuple
Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 1850.90)
print(account.name)
print(account.balance)


###deque###
#The deque class is a subclass of the list class. It is used
#to create double-ended queues, which are lists that can be
#added to or removed from at both ends.
#The deque class takes an iterable as an argument and returns
#a double-ended queue with the elements of the iterable.
#The deque class has methods called appendleft(), popleft(),

from collections import deque
friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')
print(friends)

friends.pop()

friends.popleft()