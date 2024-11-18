
friends = ("Rolf", "anne", "John")

counter = 0
for friends in friends:
    print(counter)
    print(friends)
    counter = counter + 1
#instead for this we can use enumerate fun

friends = ["Rolf", "anne", "John"]

for counter, friend in enumerate(friends):
    print(counter)
    print(friend)
# print with list
print(list(enumerate(friends)))   
# we can use  dict to enumerate same as list output
print(dict(enumerate(friends))) 