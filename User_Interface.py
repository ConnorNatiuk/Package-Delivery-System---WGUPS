from datetime import datetime

class User_Interface:

    """
    DESC: Contains the methods and functions for the program UI
    """

    def __init__(self, trucks_list, package_hash_table):

        """
        Initializes an instance of the User_Interface, takes in a list of trucks and
        the package hash table for output of information (list mileage totals and package information)

        Args:
            trucks_list (list): Passes in the list of truck objects
            package_hash_table (list): Passes in a hash table of Package objects
        """
        self.trucks_list = trucks_list
        self.package_hash_table = package_hash_table

    def run(self):
        """
        Runs the program, calls the main_menu method and determines if the program
        is running or is terminated.
        """
        in_program = True #Represents if the program is still running or has terminated.
        while in_program: #Uses a while loop to indefinitely run the program until 'e' has been chosen
            self.main_menu()
            choice = input(">>> ").lower()
            if choice == '1':
                print("\n")                     ### DISPLAYS THE TOTAL MILEAGE OF THE TRUCKS ###
                self.get_total_mileage()
                forward = input("\nPress any key to continue...\n")
                if forward:
                    continue
            elif choice == '2':
                print("\n")
                self.get_package_information()  ### DISPLAYS ALL PACKAGE INFORMATION BASED ON TIME ###
                forward = input("\nPress any key to continue...\n")
                if forward:
                    continue
            elif choice == '3':
                print("\n")
                self.view_delivery_information() ### DISPLAYS FINAL DELIVERY LOGS OF ALL PACKAGES AFTER DELIVERANCE ###
                forward = input("\nPress any key to continue...\n")
                if forward:
                    continue
            elif choice == '4':
                print("\n")
                self.get_specific_package_information() ### DISPLAYS A SPECIFICS PACKAGE INFORMATION ###
                forward = input("\nPress any key to continue...\n")
                if forward:
                    continue
            elif choice == 'e':
                print("\n")
                print("Goodbye!")
                in_program = False

    
    def main_menu(self):

        """
        Displays the main menu and lists options.
        """

        print("=" * 35)
        print("        SELECT AN OPTION")
        print("=" * 35)
        print("1. Get truck mileage information [1]")
        print("2. Get delivery status based on time [2]")
        print("3. Get final delivery logs [3]")            
        print("4. Get single package information [4]")
        print("5. Exit [E]")

    def get_total_mileage(self):

        """
        Displays total mileage for all trucks in trucks_list and mileage for each individual truck
        """

        total_mileage = 0.0
        for truck in self.trucks_list:
            total_mileage += truck.truck_mileage
        print("=" * 35)
        print("           MILEAGE INFO")
        print("=" * 35)
        print(f"Total mileage for all trucks: {total_mileage:.2f} miles")
        print(f"Truck 1: {self.trucks_list[0].truck_mileage:.2f}")
        print(f"Truck 2: {self.trucks_list[1].truck_mileage:.2f}")
        print(f"Truck 3: {self.trucks_list[2].truck_mileage:.2f}")

    def get_package_information(self):

        """
        Displays package delivery information based on an entered hour and minute.
        """

        user_time = input("Enter in time (HH:MM): ")
        try:
            (hour, minute) = user_time.split(':') #Stores the hour and minute using the ':' as a delimiter, the user must enter the time in the proper format
            selected_time = datetime(2026, 3, 5, int(hour), int(minute), 0) #Stores the selected time inside a variable for future use
        except ValueError:
            print("Invalid format. Please use HH:MM.")
            return
    
        print("=" * 35)
        print("       PACKAGE STATUS INFO")
        print("=" * 35)

        for package in range(1, 41):
            curr_package = self.package_hash_table.lookup_data(package)
            if "Delayed" in curr_package.special_notes:
                if selected_time < datetime(2026, 3, 5, 9, 5, 0):
                    package_status = "Delayed"
                    print(f"Package ID: {curr_package.package_id:3} | Address: {curr_package.package_address:40} | Status: {package_status:20}")
                    continue
            if curr_package.package_id == 9:
                if selected_time < datetime(2026, 3, 5, 10, 20, 0):
                    curr_package.package_address = "300 State St"
                    curr_package.package_zip = "84103"                  
                else:                                                   ### Changes the data for package #9 based on its changing condition depending on the time
                    curr_package.package_address = "410 S. State St"    ### (WGUPS gets the changed address after 10:20)
                    curr_package.package_zip = "84111"
            if curr_package.departure_time >= selected_time:
                package_status = "At Hub"
            elif curr_package.delivery_time > selected_time and curr_package.departure_time < selected_time:
                package_status = "En Route"
            else:
                package_status = "Delivered"
            curr_package.delivery_status = package_status #Changes the current packages delivery status based on the previous branches
            if curr_package.delivery_status == "Delivered":
                delivery_str = curr_package.delivery_time.strftime("%H:%M") if curr_package.delivery_time else "N/A"
                print(f"Package ID: {curr_package.package_id:3} | Address: {curr_package.package_address:40} | Status: {curr_package.delivery_status:} at {delivery_str}") #If the package is delivered, this displays the delivery time.
                continue
            print(f"Package ID: {curr_package.package_id:3} | Address: {curr_package.package_address:40} | Status: {curr_package.delivery_status:20}") #If it is not delivered, it displays the package information in this format.

    def get_specific_package_information(self):

        """
        Gets a specific package's information based on a user-input package ID
        """
        package_index = int(input("Enter in the package ID: "))
        curr_package = self.package_hash_table.lookup_data(package_index)
        print(curr_package)

    def view_delivery_information(self):
        
        """
        Displays the final delivery information including the package ID, address, and the departure and arrival time.
        """

        print("=" * 35)
        print("       FINAL DELIVERY LOGS")
        print("=" * 35)
        for package in range(1, 41):
            curr_package = self.package_hash_table.lookup_data(package) #Lists through all packages
            print(curr_package)
    




