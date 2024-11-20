cars = [
    
    {"make": "Ford", "model": "Fiesta", "Mileage": 230000, "fuel_consumed": 450},
    {"make": "Mazda", "model": "MX-5", "Mileage": 80000, "fuel_consumed": 50},
    {"make": "Ford", "model": "Focus", "Mileage": 290000, "fuel_consumed": 650},
    {"make": "Mini", "model": "cooper", "Mileage": 150000, "fuel_consumed": 850},
]

def calculate_mpg(car):
    mpg = round(car["Mileage"] / car["fuel_consumed"], 2)
    return mpg

def car_model(car):
    car_make= car["make"]
    car_model= car["model"]
    car_name= f"{car_make} {car_model}"
    return car_name

for car in cars:
#here car is  a argument
     car_mpg= calculate_mpg(car)
     car_kpg= round(1.60 * car_mpg, 2)
     car_name= car_model(car)
     print(f"{car_name} does {car_mpg} miles per gallon or {car_kpg} km per gallon")
