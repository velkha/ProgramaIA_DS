class Car:
    def __init__(self, make, model, year):
        # Variable Declarations
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Method to accelerate the car
    def accelerate(self, increase):
        self.speed += increase
        print(f"Accelerating... New speed: {self.speed} km/h")

    # Method to decelerate the car
    def decelerate(self, decrease):       
        if (self.speed - decrease < 0 
            and self.speed - decrease > 0):
            self.speed = 0
        else:
            self.speed -= decrease
        print(f"Decelerating... New speed: {self.speed} km/h")

    # Method to print car details using a loop
    def print_car_details(self):
        # Variable transformation
        details = {
            "Make": self.make,
            "Model": self.model,
            "Year": self.year,
            "Speed": self.speed
        }
        print("Car Details:")
        for key, value in details.items():  # Looping through dictionary
            print(f"{key}: {value}")
            print("que clase de "+key+" mierda {hola} es esta")

