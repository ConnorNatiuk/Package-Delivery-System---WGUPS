from Hash_Table import Hash_Table
from Data_Retrieval import Data_Retrieval

def main():
    print("=" * 68)
    print("Welcome to WGU Package Delivery Service. Press an option to continue")
    print("=" * 68)

    package_hash_table = Hash_Table(40)
    location_hash_table = Hash_Table(27)

    retrieval_obj = Data_Retrieval()
    retrieval_obj.get_package_data('Data/Packages.csv', package_hash_table)
    retrieval_obj.get_location_data('Data/Locations.csv', location_hash_table)
    distance_list = retrieval_obj.get_distance_data('Data/Distances.csv')

    print("\n")

    for package in range(41):
        result = package_hash_table.lookup_data(package)
        print(result)

    

if __name__ == "__main__":
    main()
