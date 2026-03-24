from Data_Retrieval import Data_Retrieval
from datetime import timedelta

class Nearest_Neighbor_Algorithm:

    def __init__(self, distance_info, location_info):
        self.distance_info = distance_info
        self.location_info = location_info
    
    def deliver_packages(self, current_truck, distance_list):
        retrieval_obj = Data_Retrieval()
        current_location = 0 #At the hub

        locations_unvisited = []
        for location in current_truck.truck_packages:
            locations_unvisited.append(location)
        
        while len(locations_unvisited) > 0: #If true there are still packages
            next_package = None
            min_distance = 100.0

            for package in locations_unvisited:
                index = package.package_address_index
                distance = retrieval_obj.get_distance_between(current_location, index, distance_list)

                if float(distance) <= min_distance:
                    min_distance = float(distance)
                    next_package = package
            
            current_truck.truck_mileage += min_distance
            minutes_traveled = current_truck.get_minutes_traveled(min_distance)
            current_truck.current_time += timedelta(minutes=minutes_traveled)
            current_location = next_package.package_address_index

            next_package.delivery_status = "Delivered"
            next_package.delivery_time = current_truck.current_time

            locations_unvisited.remove(next_package)
            # print(f"Delivered -> {next_package}")
        
        distance_back = retrieval_obj.get_distance_between(current_location, 0, distance_list)
        current_truck.truck_mileage += float(distance_back)
        current_truck.current_location = 0