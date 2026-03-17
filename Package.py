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

    def insert(self, package_id, package_address, package_city, package_state, package_zip, package_deadline, package_weight, special_notes, delivery_status):
        package_data = [package_id, package_address, package_city, package_state, package_zip, package_deadline, package_weight, special_notes, delivery_status]
    
    #GETTERS AND SETTERS
    
    def get_package_id(self):
        return self.package_id
    def set_package_id(self, package_id):
        self.package_id = package_id
    def get_package_address(self):
        return self.package_address
    def set_package_address(self, package_address):
        self.package_address = package_address
    def get_package_city(self):
        return self.package_city
    def set_package_city(self, package_city):
        self.package_city = package_city
    def get_package_state(self):
        return self.package_state
    def set_package_state(self, package_state):
        self.package_state = package_state
    def get_package_zip(self):
        return self.package_zip
    def set_package_zip(self, package_zip):
        self.package_zip = package_zip
    def get_package_deadline(self):
        return self.package_deadline
    def set_package_deadline(self, package_deadline):
        self.package_deadline = package_deadline
    def get_package_weight(self):
        return self.package_weight
    def set_package_weight(self, package_weight):
        self.package_weight = package_weight
    def get_special_notes(self):
        return self.special_notes
    def set_special_notes(self, special_notes):
        self.special_notes = special_notes
    def get_delivery_status(self):
        return self.delivery_status
    def set_delivery_status(self, delivery_status):
        self.delivery_status = delivery_status
