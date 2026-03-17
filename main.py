from Hash_Table import Hash_Table
from Data_Retrieval import Data_Retrieval
from Package import Package

def main():
    print("=" * 68)
    print("Welcome to WGU Package Delivery Service. Press an option to continue")
    print("=" * 68)

    data_hash_table = Hash_Table(10)

    retrieval_obj = Data_Retrieval()
    retrieval_obj.get_package_data('Data/Packages.csv', data_hash_table)

if __name__ == "__main__":
    main()
