from datetime import datetime, timedelta

class Truck:

    """
    DESC: Represents a truck object that loads and delivers packages to their destination.

    Attributes:
        truck_id (int): The identification number of the truck
        truck_mileage (float): The mileage updated and tracked for each truck
        truck_packages (list): A list containing the packages to be loaded onto the truck
        truck_speed (int): A constant representing the speed at which the truck travels
        truck_capacity (int): A constant representing the package capacity for the truck
        is_empty (bool): Status indicating if the truck has packages on it
        current_time (datetime): The current time of the truck
        current_location (int): An index representing a location where the truck is at
    """

    """
    GLOBAL ATTRIBUTES:
    """
    MAX_TRUCK_CAPACITY = 16 #packages
    TRUCK_SPEED = 18 #mph

    def __init__(self, truck_id, truck_mileage=0, truck_speed=TRUCK_SPEED, truck_capacity=MAX_TRUCK_CAPACITY):

        """ 
        Initializes a new truck instance
        
        ARGS:
            truck_id: The truck identifier as an integer
            truck_mileage: Initialized at 0
            truck_packages: A list containing the packages to be loaded onto the truck
            truck_speed: Truck speed is set to 18
            truck_capacity: Truck capacity is set to 16
            is_empty: Status initially set to true
            current_time: Starting at 8:00am
            current_location: a location index initialized at the hub for each truck
        
        """
        self.truck_id = truck_id
        self.truck_mileage = truck_mileage
        self.truck_packages = [] #MAX of 16
        self.truck_speed = truck_speed
        self.truck_capacity = truck_capacity
        self.is_empty = True
        self.current_time = datetime(2026, 3, 5, 8, 0, 0, 0) #Initial time set to 8:00AM for all trucks, changes depending on the main method.
        self.current_location = 0 #The Hub
    
    def load_package(self, package):
        """
        Loads a package onto the corresponding truck

        ARGS:
            self: refers to itself
            package: takes in an Package object
        """
        if len(self.truck_packages) == self.truck_capacity: #If the amount of items inside truck_packages has reached 16
           print("Your truck is full!")
           return False
        else:
           self.truck_packages.append(package) #Loads the package into that specific truck's truck_packages list
           self.is_empty = False #The truck is no longer empty
           return True
    
    def get_minutes_traveled(self, distance_traveled):

        """
        Returns the minutes taken to travel based on a distance passed into the method

        ARGS:
            self: refers to itself
            distance_traveled (float): Refers to the distance traveled between one location and another
        """

        miles_per_minute = 0.3 #Calculated based on how many miles are traveled per 60 minutes at 18mph
        time_taken = distance_traveled / miles_per_minute
        return time_taken
    
    def drive_to_address(self, traveled_distance, next_location):

        """
        Updates the truck location, mileage, and current time based on the next location it will go to.

        ARGS:
            self: refers to itself
            traveled_distance (float): The current distance the truck has driven (mileage)
            next_location: An index of the next location, where the truck will travel next to as determined by the NNA
        """

        self.truck_mileage += traveled_distance #Updates the mileage
        time_taken = self.get_minutes_traveled(traveled_distance) #Calculates the time taken to drive from one location to another based on distance
        self.current_time += timedelta(minutes=time_taken) #Updates time delta

        self.current_location = next_location #"Drives" to the next location, updates it's location.



    
