from Hash_Table import Hash_Table
from Data_Retrieval import Data_Retrieval
from Truck import Truck
from datetime import datetime, timedelta
from Nearest_Neighbor_Algorithm import Nearest_Neighbor_Algorithm
from User_Interface import User_Interface

"""
DESC: Contains the main method and the logic that will be implemented in running the algorithm
"""
def logic():
    """
    Contains the logic for the program from creating the hash tables, retrieving data, and loading
    and delivering packages. Implements the nearest neighbor algorithm and contains package status and delivery
    information.
    """
    package_hash_table = Hash_Table(40) #Creates the hash table for the packages. Uses 40 as the default bucket size, if other packages are added there is linear probing collision handling.
    location_hash_table = Hash_Table(27) #Creates a hash table for the locations so that the data is stored and accessed more easily. Does however create more memory overhead.

    retrieval_obj = Data_Retrieval() #Instantiates Data Retrieval object
    location_table = retrieval_obj.get_location_data('Data/Locations.csv', location_hash_table)
    retrieval_obj.get_package_data('Data/Packages.csv', package_hash_table, location_table) ### Retrieves data and assigns each retrieval to a variable
    distance_list = retrieval_obj.get_distance_data('Data/Distances.csv')

    TRUCK_ONE = Truck(1)
    TRUCK_TWO = Truck(2)  ### Instantiates trucks with corresponding IDs
    TRUCK_THREE = Truck(3)
    truck_list = [TRUCK_ONE, TRUCK_TWO, TRUCK_THREE] #Creates a list of truck objects to return for finalized truck information
    
    algorithm = Nearest_Neighbor_Algorithm(distance_list, location_table) #Instantiates an instance of the main algorithm

    truck_two_start_time = datetime(2026, 3, 5, 9, 5, 0) #Sets start time for truck 2
    TRUCK_TWO.current_time = truck_two_start_time + timedelta(minutes=5) #Adds 5 minutes for loading time

    truck_one_package_ids = [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    truck_two_package_ids = [3, 6, 7, 8, 10, 11, 12, 17, 18, 21, 22, 25, 28, 32, 36, 38] ### LISTS VALID PACKAGES FOR EACH TRUCK BASED ON CONDITIONS ###
    truck_three_package_ids = [9, 23, 24, 26, 27, 33, 35, 39]

    for package in truck_one_package_ids:
        """
        Loads packages for truck one, changes package status
        """
        current_package = package_hash_table.lookup_data(package)
        current_package.delivery_status = "En Route"
        current_package.departure_time = TRUCK_ONE.current_time + timedelta(minutes=5) #Adds 5 minutes to initial time for loading and departure
        TRUCK_ONE.load_package(current_package)
    
    for package in truck_two_package_ids:
        """
        Loads packages for truck two, changes package status
        """
        current_package = package_hash_table.lookup_data(package)
        current_package.delivery_status = "En Route"
        current_package.departure_time = TRUCK_TWO.current_time
        TRUCK_TWO.load_package(current_package)

    algorithm.deliver_packages(TRUCK_ONE, distance_list) ### DELIVERS PACKAGES FOR THE FIRST TWO TRUCKS,
    algorithm.deliver_packages(TRUCK_TWO, distance_list) ### so that one of the first trucks can return and a driver can take the third truck

    TRUCK_THREE.current_time = datetime(2026, 3, 5, 10, 25, 0) #Sets the time to when the last package address is changed and all packages are ready to be delivered.

    for package in truck_three_package_ids:
        """
        Loads packages for truck three, changes package status
        """
        current_package = package_hash_table.lookup_data(package)
        if current_package.package_id == 9: #This handles the changing address for package ID 9 when the third truck is loaded.
            current_package.package_address = "410 S. State St"
            current_package.package_zip = "84111"
            current_package.package_address_index = 19
        current_package.delivery_status = "En Route"
        current_package.departure_time = TRUCK_THREE.current_time #5 minutes for loading and departure already accounted for
        TRUCK_THREE.load_package(current_package)
    
    algorithm.deliver_packages(TRUCK_THREE, distance_list) #DELIVERS THE THIRD TRUCK'S PACKAGES

    return truck_list, package_hash_table #Returns the truck list and the package hash table for output of finalized data
    
def main():
    """
    Runs the logic method and the user interface.
    """
    print("=" * 68)
    print("             Welcome to WGU Package Delivery Service!")
    print("=" * 68)

    truck_list, package_hash_table = logic() #Assigns the return values of the logic method to truck_list and package_hash_table
    ui = User_Interface(truck_list, package_hash_table) #Instantiates the user interface passing in the data from the final return values of the truck list and package hash table.

    ui.run() #Runs the UI


if __name__ == "__main__":
    main()
