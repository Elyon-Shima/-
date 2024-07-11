# Question 3: Transport Fleet Management System 
class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.registration_number} - {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"Car: {super().__str__()}, Seats: {self.number_of_seats}"

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return f"Truck: {super().__str__()}, Cargo Capacity: {self.cargo_capacity} tons"

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def __str__(self):
        return f"Motorcycle: {super().__str__()}, Engine Capacity: {self.engine_capacity} cc"

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def search_vehicle_by_registration_number(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle
        return None

# Part 4
fleet = Fleet()

fleet.add_vehicle(Car("KDC123N", "Toyota", "Land Cruiser LC200", 7))
fleet.add_vehicle(Truck("KCZ555R", "Mercedes-Benz", "Actross", 20))
fleet.add_vehicle(Motorcycle("KMGZ001A", "Yamaha", "MT-07", 689))

print("All vehicles in the fleet:")
fleet.display_all_vehicles()

print("\nSearch for a vehicle with registration number 'KDC123N':")
vehicle = fleet.search_vehicle_by_registration_number("KDC123N")
if vehicle:
    print(vehicle)
else:
    print("Vehicle not found.")

