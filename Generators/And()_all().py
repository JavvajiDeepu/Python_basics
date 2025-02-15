friends = [
    {'name': 'Rolf', 'location': 'Washington'},
    {'name': 'Jose', 'location': 'San Francisco'},
    {'name': 'Randy', 'location': 'Washington'},
    {'name': 'Anna', 'location': 'San Francisco'},
    {'name': 'Mary', 'location': 'Washington'},
]
your_location = input('Where are you right now? ')
friends_nearby = [friends for friend in friends if friend['location'] == your_location]

if any(friends_nearby): # if friends_nearby is not empty#all can be used to check if all elements in a list are True
    print('You are not alone!')
print(all([0, 1, 2, 3, 4])) 

