from Package import Package
from Location import Location
import csv

class Data_Retrieval:

    """
    DESC: Handles ingestion from CSV files, an utilizes the hash table class to create hash tables of the package and location
    data. Includes other methods such as get_distance_between and enables for other methods to be added if necessary.
    """

    def get_package_data(self, file, hash_table, locations):

        """
        Reads data from a CSV file (in this case the Packages.csv file) and creates Package objects which
        it will then add to the respective hash table passed in.
        """

        with open(file, mode='r') as package_file:
            package_data = csv.reader(package_file)

            header = next(package_data) # Skips the header row (stores it as a variable if needed for reference)

            for row in package_data:
                package_id = int(row[0])
                package_address = row[1]
                package_city = row[2]
                package_state = row[3]                  ### Assigns values to variables according to the values inside the columns of each row of the CSV file ###
                package_zip = row[4]
                package_del_deadline = row[5]
                package_weight = row[6]
                package_spec_notes = row[7]
                package_status = "At Depot"

                package = Package(package_id, package_address, package_city, package_state, package_zip, 
                                  package_del_deadline, package_weight, package_spec_notes, package_status) #Creates a package object based on the ingested data
                
                for i, location in enumerate(locations): #Takes passed in location table and assigns an integer to each location each loop
                    if package_address in location: #Checks if the package_address string is inside the location object
                        package.package_address_index = i #If the location contains the address string, it will assign the package object with that specific package address index
                        break
                    
                hash_table.insert(package_id, package) #Inserts the package into the hash table, with the key being the package id.
    
    def get_distance_data(self, file):

        """
        Returns a list of distances between each location, read in from the Distances.csv file.
        """

        distance_list = [] #Creates a new list to store the distances inside of. Unlike the others, it will not be stored in a hash table.
        with open(file, mode='r') as distance_file:
            distance_data = csv.reader(distance_file) #Ingests in the CSV file into a variable

            header = next(distance_data) #Skips the first row of distances.csv, stored as a variable in case of future reference

            for row in distance_data:
                distance_list.append(row) ### Appends each row of data to the distance_list, which will primarily be accessed inside of the get_distance_between method.
        return distance_list #Returns the now created distance list.
    
    def get_location_data(self, file, hash_table):

        """
        Reads data from a CSV file (in this case the Locations.csv file) and creates Location objects which
        it will then add to the respective hash table passed in.

        Returns a list of location addresses that will be referenced in the get_package_data method.
        """

        location_list = [] #Creates a list to store the location addresses (which will be used to find the address index for each package)
        with open(file, mode='r') as location_file:
            location_data = csv.reader(location_file) #Ingests in the CSV file into a variable
            
            header = next(location_file) #Skips the first row of distances.csv, stored as a variable in case of future reference

            for row in location_data:
                location_id = int(row[0])
                location_name = row[1]      ### Assigns values to variables according to the values inside the columns of each row of the CSV file ###
                location_address = row[2]

                location = Location(location_id, location_name, location_address) #stores a Location object created from the data into a location variable

                hash_table.insert(location_id, location) #The location is stored into the hash table, the key being the location_id
                location_list.append(location_address) #The location address is appended to the location list
        return location_list
    
    def get_distance_between(self, address_1, address_2, distance_list):

        """
        Passes in 2 addresses, and then utilizes the distance list created earlier to find the distance
        between the two addresses.
        """

        if address_1 < address_2:                       ####
            address_1, address_2 = address_2, address_1 #Handles IndexErrors and EmptyValue errors if the first address passed in has a lesser index than the second address.
        
        distance = distance_list[address_1][address_2] #Grabs the distance from the distance list (matrix) created.
        return distance
