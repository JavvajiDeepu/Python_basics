friends_last_seen = {               #dictionary is mutable
    'Rolf': 31, 
    'Jose': 2,      
    'Randy': 300
}
def see_friend(friends, name, day):
    print(id(friends))
    friends[name] = day
#print(id(friends_last_seen))
#print(id(friends_last_seen['Rolf']))

see_friend(friends_last_seen, 'Rolf', 0)

##print(id(friends_last_seen))

age = 30
def increase_age(current_age):
    
    current_age = current_age + 1
    print(id(current_age))
    return current_age

print(id(age))
new_age = increase_age(age)
print(id(new_age))
print(id(age))
#The id of age does not change because it is immutable
#The id of current_age changes because it is a local variable
#The id of new_age changes because it is a local variable
#The id of friends does not change because it is mutable
#The id of friends_last_seen does not change because it is mutable
#The id of friends_last_seen['Rolf'] does not change because it is mutable
#The id of friends_last_seen changes because it is a local variable
#The id of friends_last_seen['Rolf'] changes because it is a local variable

primes = [2, 3, 5, 7, 11]   #list is mutable        
print(id(primes))
primes += [13, 17]  #list is mutable
print(id(primes))   
primes = primes + [13, 17] #list is mutable 
print(id(primes))
#The id of primes does not change because it is mutable
