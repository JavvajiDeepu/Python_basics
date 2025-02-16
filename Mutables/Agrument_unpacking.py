accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}
def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.90, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings')
]

for t in transactions:
    #add_balance(t[0], t[1])
    add_balance(*t)#unpacking the tuple #*t is the unpacking operator for the tuple t   
    add_balance(amount=t[0], name=t[1])#named arguments   
    print( (accounts))#id of the dictionary is same     

class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
    
]
#user_objects = [user(username=data['username'], password=data['password'])]

for data in users:
    print(user(**data)for data in users)#unpacking the dictionary

