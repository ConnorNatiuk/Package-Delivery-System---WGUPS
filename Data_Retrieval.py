from Package import Package
from Location import Location
import csv

class Data_Retrieval:
    def get_package_data(self, file, hash_table):
        with open(file, mode='r') as package_file:
            package_data = csv.reader(package_file)

            header = next(package_data)

            for row in package_data:
                package_id = int(row[0])
                package_address = row[1]
                package_city = row[2]
                package_state = row[3]
                package_zip = row[4]
                package_del_deadline = row[5]
                package_weight = row[6]
                package_spec_notes = row[7]
                package_status = "At Depot"

                # print(row[1])

                package = Package(package_id, package_address, package_city, package_state, package_zip, 
                                  package_del_deadline, package_weight, package_spec_notes, package_status)
                
                hash_table.insert(package_id, package)

        print("Successfully loaded packages")
    
    def get_distance_data(self, file):
        distance_list = []
        with open(file, mode='r') as distance_file:
            distance_data = csv.reader(distance_file)

            header = next(distance_data)

            for row in distance_data:
                distance_list.append(row)
        
        print("Successfully loaded distances")
        return distance_list
    
    def get_location_data(self, file, hash_table):
        location_list = []
        with open(file, mode='r') as location_file:
            location_data = csv.reader(location_file)
            
            header = next(location_file)

            for row in location_data:
                location_id = int(row[0])
                location_name = row[1]
                location_address = row[2]

                location = Location(location_id, location_name, location_address)

                hash_table.insert(location_id, location)
            
        print("Successfully loaded locations")
