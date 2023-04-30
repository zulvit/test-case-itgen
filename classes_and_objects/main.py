class Autobus:
    def __init__(self, start_point, end_point, route_number, travel_time):
        self.start_point = start_point
        self.end_point = end_point
        self.route_number = route_number
        self.travel_time = travel_time

    def __str__(self):
        return f"Autobus {self.route_number} from {self.start_point} to {self.end_point}, travel time: {self.travel_time} minutes."

    def get_start_point(self):
        return self.start_point

    def set_start_point(self, start_point):
        self.start_point = start_point

    def get_end_point(self):
        return self.end_point

    def set_end_point(self, end_point):
        self.end_point = end_point

    def get_route_number(self):
        return self.route_number

    def set_route_number(self, route_number):
        self.route_number = route_number

    def get_travel_time(self):
        return self.travel_time

    def set_travel_time(self, travel_time):
        self.travel_time = travel_time


bus1 = Autobus("New York", "Boston", 123, 240)
print(bus1)

bus1.set_start_point("Chicago")
bus1.set_travel_time(300)
print(bus1.get_start_point())
print(bus1.get_travel_time())
