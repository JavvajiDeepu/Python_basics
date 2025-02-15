friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
starts_with_r = filter(lambda x: x.startswith('R'), friends)
another_starts_with_r = (f for x in friends if x.startswith('R'))

friends_lower = map(lambda x: x.lower(), friends)
friends_lower = [friend.lower() for friend in friends]
friends_lower = (friend.lower() for friend in friends)

print(next(friends_lower))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])
    def __repr__(self):
        return f'<User {self.username}>'
users = [       
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}               
]   
users = [User.from_dict(user) for user in users]
# this will print [<User rolf>, <User tecladoisawesome>]
#print(users)  # this will print [<User rolf>, <User tecladoisawesome>]
users = map(User.from_dict, users)

#print(next(users)) # this will print <User rolf>