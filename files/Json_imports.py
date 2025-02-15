import json

File = open('friends_json.txt', 'r')
file_contents = json.load(File) # read file and turns it to dictonary  load
File.close()
print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file) # 
file.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string) 
#dump function that writes the dictionary directly to a file in the form of JSON without having to convert it to an actual JSON object
print(incorrect_car[0]['name'])