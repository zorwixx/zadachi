class Plane:
    def __init__(self, name, max_speed, flight_range):
        self.name = name
        self.max_speed = max_speed
        self.flight_range = flight_range

    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Макс_швидкість: {self.max_speed} км/год")
        print(f"Дальність_польоту: {self.flight_range}")

plane = Plane("Літак", 300)

plane.display_info()