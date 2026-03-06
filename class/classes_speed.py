class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0

    def acceleration(self, increment):
        self._speed += increment

    def display_status(self):
        print(f"{self.brand} is running at {self._speed} km/h.")

if __name__ == "__main__":
    car = Car("Toyota", "Corolla")
    car.acceleration(50)
    car.display_status()
        