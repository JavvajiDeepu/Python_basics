
#def starts_with_r(friend):
    #return friend.startswith('R')
def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i
friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
starts_with_r = my_custom_filter(lambda x: x.startswith('R'), friends)
print(next(starts_with_r))
print(list(starts_with_r))

""""
def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i 
            """

friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
starts_with_r = my_custom_filter(lambda x: x.startswith('R'), friends)
print(next(starts_with_r))
print(list(starts_with_r))

def my_custom_filter(func, iterable):
                for i in iterable:
                    if func(i):
                        yield i