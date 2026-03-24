from Data_Retrieval import Data_Retrieval
from datetime import timedelta

class Nearest_Neighbor_Algorithm:
    """
    DESC: A greedy heuristic that iteratively looks for the nearest location in a list of unvisited locations,
    and delivers the corresponding package. It updates truck information, delivery status, and delivery time. Once all
    packages have been delivered, it calculates and updates the time and mileage it takes to drive back to the hub.
    """

    def __init__(self, distance_info, location_info):
        
        """
        Initializes an instance of the the Nearest Neighbor Algorithm class

        Args:
            distance_info (list): Passes in a list of distances and corresponding indices
            location_info (list): Passes in a table containing location information
        """

        self.distance_info = distance_info
        self.location_info = location_info
    
    def deliver_packages(self, current_truck, distance_list):

        """
        Implements the logic of a Nearest Neighbor Algorithm to deliver packages on any given truck.
        Passes in a distance list to figure out the next location, track mileage, and update time.
        
        """

        retrieval_obj = Data_Retrieval() #Creates a data retrieval object
        current_location = 0 #All trucks start at the hub

        locations_unvisited = [] #Creates an empty list of unvisited locations
        for location in current_truck.truck_packages:
            locations_unvisited.append(location) #Appends packages in (with subsequent location data) to track unvisited locations
        
        while len(locations_unvisited) > 0: #If true there are still packages
            next_package = None #Initially doesn't have a next package to deliver
            min_distance = 100.0 #Initial distance set high so that the next package distance will automatically be lower.

            for package in locations_unvisited: #Iterates through packages in locations_unvisited list
                index = package.package_address_index
                distance = retrieval_obj.get_distance_between(current_location, index, distance_list) #Finds distance between the current truck location and the 
                                                                                                      #location of the next package
                if float(distance) <= min_distance:
                    min_distance = float(distance) #Distance is tracked so that the next location will be dependent on the least amount of distance to deliver the next package.
                    next_package = package #The package at the end of the for loop will have the least distance to the next location
            
            current_truck.truck_mileage += min_distance #Updates truck mileage based on distance to the next package
            minutes_traveled = current_truck.get_minutes_traveled(min_distance)
            current_truck.current_time += timedelta(minutes=minutes_traveled) #Updates the current trucks time based on the minutes traveled
            current_location = next_package.package_address_index #Updates the current location in the method based on the next package's address index

            next_package.delivery_status = "Delivered" #The package is delivered, update status accordingly
            next_package.delivery_time = current_truck.current_time #Update the delivery time of the package to the time the truck arrived to deliver

            locations_unvisited.remove(next_package) #The location is now visited, the package is removed from locations_unvisited
        
        """
        When all packages for the specific truck are delivered, the final snippet calculates the distance back to the hub,
        else the truck would be out in the middle of nowhere and the final mileage would be wrong.
        """
        distance_back = retrieval_obj.get_distance_between(current_location, 0, distance_list)
        current_truck.truck_mileage += float(distance_back)
        current_truck.current_location = 0