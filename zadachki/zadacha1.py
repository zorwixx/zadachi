class TransportVehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Макс. швидкість: {self.max_speed} км/год")

vehicle = TransportVehicle("Автомобіль", 200)

vehicle.display_info()
