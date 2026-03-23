from Hash_Table import Hash_Table
from Data_Retrieval import Data_Retrieval
from Truck import Truck
from datetime import datetime
from NearestNeighborAlgorithm import NearestNeighborAlgorithm
 
def main():
    print("=" * 68)
    print("Welcome to WGU Package Delivery Service. Press an option to continue")
    print("=" * 68)

    THE_HUB = 0

    package_hash_table = Hash_Table(40)
    location_hash_table = Hash_Table(27)

    retrieval_obj = Data_Retrieval()
    location_table = retrieval_obj.get_location_data('Data/Locations.csv', location_hash_table)
    retrieval_obj.get_package_data('Data/Packages.csv', package_hash_table, location_table)
    distance_list = retrieval_obj.get_distance_data('Data/Distances.csv')

    TRUCK_ONE = Truck(1)
    TRUCK_TWO = Truck(2)
    TRUCK_THREE = Truck(3)
    algorithm = NearestNeighborAlgorithm(distance_list, location_table)

    truck_two_start_time = datetime(2026, 3, 5, 9, 5, 0)
    TRUCK_TWO.current_time = truck_two_start_time

    temp_package = package_hash_table.lookup_data(1)

    truck_one_package_ids = [1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    truck_two_package_ids = [3, 6, 7, 8, 10, 11, 12, 17, 18, 21, 22, 25, 28, 32, 36, 38]
    truck_three_package_ids = [9, 23, 24, 26, 27, 33, 35, 39]

    # print(temp_package)

    for package in truck_one_package_ids:
        current_package = package_hash_table.lookup_data(package)
        current_package.delivery_status = "En Route"
        current_package.departure_time = TRUCK_ONE.current_time
        print(current_package)
        TRUCK_ONE.load_package(current_package)
    
    for package in truck_two_package_ids:
        current_package = package_hash_table.lookup_data(package)
        current_package.delivery_status = "En Route"
        current_package.departure_time = TRUCK_TWO.current_time
        TRUCK_TWO.load_package(current_package)


    algorithm.deliver_packages(TRUCK_ONE, distance_list)
    

    

    

if __name__ == "__main__":
    main()
