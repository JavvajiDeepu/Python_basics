
#defening a function 
def max():
     name = input("enter your name: ")
     print(f"Hello,{name}!")

max()

# arguments and parameters
cars = [
    
    {"make": "Ford", "model": "Fiesta", "Mileage": 230000, "fuel_consumed": 450},
    {"make": "Mazda", "model": "MX-5", "Mileage": 80000, "fuel_consumed": 50},
    {"make": "Ford", "model": "Focus", "Mileage": 290000, "fuel_consumed": 650},
    {"make": "Mini", "model": "cooper", "Mileage": 150000, "fuel_consumed": 850},
]
def calculate_mpg(car):
    # here round is used for converting float values to decimals (how many decimals you need ex 2.92)
    # syntax for rounded_number = round(number, 2 or 3)
    mpg = round(car["Mileage"] / car["fuel_consumed"], 2)
    return mpg
def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name
def print_car_info(i):
    name= car_name(i)
    mpg = calculate_mpg(i)
    print(f"{name} does {mpg} miles per gallon.")
for sai in cars:
   #print(sai)
   print_car_info(sai)

# default paramters
def add(x, y=3):
    total = x+y
    return total
print(add(4 , ))

# lambda function
divide = lambda x, y: x / y
# print(lambda x, y: x / y),(23,56)
print(divide(23,56))

