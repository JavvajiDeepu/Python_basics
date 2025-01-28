class Garage:
    def __init__(self):
        self.cars =[]
    def __len__(self):
        return len(self.cars)
    def add_car(self, cars):
        raise NotImplementedError("we can't add cars to the garage yet.")
    
ford =Garage()
ford.add_car('Fiseta')
print(len(ford))