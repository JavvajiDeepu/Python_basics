# comma is mandatory for writing single tuple.
friends = ('john', 'max', 'rosa')
friends = friends + ('jack',)
print(friends)

#sets are unchanged and only can add and remove the values
max_friends = {"john", "max", "rosa"}
max_friends.add("jen")
max_friends.remove("rosa")
print(max_friends)

# difference sets (excutes only in arts and next excute only in it.common students will not excute in differnce set)
art_students = {'jack', 'rosa', 'max'}
it_students = {'max', 'anne'}
art_but_not_it = art_students.difference(it_students)
it_but_not_arts = it_students.difference(art_students)
print(art_but_not_it)
print(it_but_not_arts)

# symmertic_difference sets(who are  in arts and it, its excutes those students)
art_students = {'jack', 'rosa', 'max'}
it_students = {'max', 'anne'}
not_in_both = art_students.symmetric_difference(it_students)
print(not_in_both)

# intersection set (only who are they in both)
art_students = {'jack', 'rosa', 'max'}
it_students = {'max', 'anne'}
only_in_both = art_students.intersection(it_students)
print(only_in_both)

#union set( all students
art_students = {'jack', 'rosa', 'max'}
it_students = {'max', 'anne'}
all_students = art_students.union(it_students)
print(all_students)

# by using input function for empty set
art_students = {'jack', 'rosa', 'max'}
it_students = set()
students = input("enter students name: ")
it_students.add(students)
print(art_students.intersection(it_students))

#dictonaries key: value
name_age = {"rolf": 24, "sun": 30, "moon": 22}
print(name_age["rolf"])

#Add dictonaries more
name_age = {"rolf": 24, "sun": 30, "moon": 22}
name_age["rolf"] = 27
name_age["risk"] = 44
print(name_age)