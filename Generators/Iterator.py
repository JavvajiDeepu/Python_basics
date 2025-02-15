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
class firsthundrediterable:
    def __iter__(self):
        return firsthundredgenerator()
    
print(sum(firsthundrediterable())) # this will print 4950

# The __iter__ method is what makes an object iterable. The __next__ method is what makes an object an iterator.
                                                                                                                                                                                                                                                                                      
class Anotheriterable:
    def __init__(self):
        self.cars = ['BMW', 'Toyota', 'Ford', 'Mazda']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

for car in Anotheriterable():
    print(car) # this will print BMW Toyota Ford Mazda                                  