
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
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")
for car in cars:
    calculate_mpg(car)