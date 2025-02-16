friends_last_seen = {
    'Rolf': 31,
    'Jose': 2,
    'Randy': 300
}

print (id(friends_last_seen))
friends_last_seen['Rolf'] = 0
print (id(friends_last_seen))
my_int = 5
print(id(my_int))
my_int = my_int + 1
print(id(my_int)) #id of my_int changes because it is immutable

friends = ['Rolf', 'Jose']
print(id(friends))
friends.append('Anna')
print(id(friends)) #id of friends does not change because it is mutable