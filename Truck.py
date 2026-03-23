from datetime import datetime, timedelta


class Truck:

    MAX_TRUCK_CAPACITY = 16 #packages
    TRUCK_SPEED = 18 #mph

    def __init__(self, truck_id, truck_mileage=0, truck_speed=TRUCK_SPEED, truck_capacity=MAX_TRUCK_CAPACITY):
        self.truck_id = truck_id
        self.truck_mileage = truck_mileage
        self.truck_packages = [] #MAX of 16
        self.truck_speed = truck_speed
        self.truck_capacity = truck_capacity
        self.is_empty = True
        self.current_time = datetime(2026, 3, 5, 8, 0, 0, 0)
        self.current_location = 0 #The Hub
    
    def load_package(self, package):
        if len(self.truck_packages) == self.truck_capacity:
           print("Your truck is full!")
           return False
        else:
           self.truck_packages.append(package)
           self.is_empty = False
           return True
    
    def get_minutes_traveled(self, distance_traveled):
        miles_per_minute = 0.3
        time_taken = distance_traveled / miles_per_minute
        return time_taken
    
    def drive_to_address(self, traveled_distance, next_location):
        self.truck_mileage += traveled_distance
        time_taken = self.get_minutes_traveled(traveled_distance)
        self.current_time += timedelta(minutes=time_taken)

        self.current_location = next_location



    
