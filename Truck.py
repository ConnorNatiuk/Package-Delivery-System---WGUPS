from datetime import datetime, time


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
        self.start_time = time(hour=8,minute=0)

    
