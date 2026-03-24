from datetime import datetime

class User_Interface:

    def __init__(self, trucks_list, package_hash_table):
        self.trucks_list = trucks_list
        self.package_hash_table = package_hash_table

    def run(self):
        in_program = True
        while in_program:
            self.main_menu()
            choice = input(">>> ").lower()
            if choice == '1':
                print("\n")
                self.get_total_mileage()
                forward = input("\nPress any key to continue...\n")
                if forward:
                    continue
            elif choice == '2':
                print("\n")
                self.get_package_information()
                forward = input("\nPress any key to continue...\n")
                if forward:
                    continue
            elif choice == '3':
                print("\n")
                self.view_delivery_information()
                forward = input("\nPress any key to continue...\n")
                if forward:
                    continue
            elif choice == '4':
                print("\n")
                self.get_specific_package_information()
                forward = input("\nPress any key to continue...\n")
                if forward:
                    continue
            elif choice == 'e':
                print("\n")
                print("Goodbye!")
                in_program = False

    
    def main_menu(self):
        print("=" * 35)
        print("        SELECT AN OPTION")
        print("=" * 35)
        print("1. Get truck mileage information [1]")
        print("2. Get delivery status based on time [2]")
        print("3. Get final delivery logs [3]")
        print("4. Get single package information [4]")
        print("5. Exit [E]")

    def get_total_mileage(self):
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
        user_time = input("Enter in time (HH:MM): ")
        try:
            (h, m) = user_time.split(':')
            selected_time = datetime(2026, 3, 5, int(h), int(m), 0)
        except ValueError:
            print("Invalid format. Please use HH:MM.")
            return
    
        print("=" * 35)
        print("       PACKAGE STATUS INFO")
        print("=" * 35)

        for package in range(1, 41):
            curr_package = self.package_hash_table.lookup_data(package)
            if curr_package.package_id == 9:
                if selected_time < datetime(2026, 3, 5, 10, 20, 0):
                    curr_package.package_address = "300 State St"
                    curr_package.package_zip = "84103"
                else:
                    curr_package.package_address = "410 S. State St"
                    curr_package.package_zip = "84111"
            if curr_package.departure_time >= selected_time:
                package_status = "At Hub"
            elif curr_package.delivery_time > selected_time and curr_package.departure_time < selected_time:
                package_status = "En Route"
            else:
                package_status = "Delivered"
            curr_package.delivery_status = package_status
            if curr_package.delivery_status == "Delivered":
                delivery_str = curr_package.delivery_time.strftime("%H:%M") if curr_package.delivery_time else "N/A"
                print(f"Package ID: {curr_package.package_id:3} | Address: {curr_package.package_address:40} | Status: {curr_package.delivery_status:} at {delivery_str}")
                continue
            print(f"Package ID: {curr_package.package_id:3} | Address: {curr_package.package_address:40} | Status: {curr_package.delivery_status:20}")

    def get_specific_package_information(self):
        package_index = int(input("Enter in the package ID: "))
        curr_package = self.package_hash_table.lookup_data(package_index)
        print(curr_package)

    def view_delivery_information(self):
        print("=" * 35)
        print("       FINAL DELIVERY LOGS")
        print("=" * 35)
        for package in range(1, 41):
            curr_package = self.package_hash_table.lookup_data(package)
            print(curr_package)
    




