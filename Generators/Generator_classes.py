class firsthundredgenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):  # this is the method that makes an object iterable
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
      
              raise StopIteration()

    def __iter__(self):  # this is the method that makes an object an iterator
        return self
my_gen = firsthundredgenerator()
print(next(my_gen))
print(next(my_gen)) 

for i in firsthundredgenerator():
    print(i)     # this will print 0 to 99   # this will print 0 to 99   # this will print 0 to 99    

# The __iter__ method is what makes an object iterable. The __next__ method is what makes an object an iterator.       