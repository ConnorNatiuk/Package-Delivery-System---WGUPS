import csv

class Package:

    def __init__(self, package_id, package_address, package_city, package_state,
                 package_zip, package_deadline, package_weight, special_notes, delivery_status):
        self.package_id = package_id
        self.package_address = package_address
        self.package_city = package_city
        self.package_state = package_state
        self.package_zip = package_zip
        self.package_deadline = package_deadline
        self.package_weight = package_weight
        self.special_notes = special_notes
        self.delivery_status = delivery_status

    def __str__(self):
        return (f"Package_ID: {self.package_id:3} | Address: {self.package_address:40} | Status: {self.delivery_status:20} | Notes: {self.special_notes:70}")
        
                