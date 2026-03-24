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

        self.package_address_index = None
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        departure_str = self.departure_time.strftime("%H:%M") if self.departure_time else "N/A"
        delivery_str = self.delivery_time.strftime("%H:%M") if self.delivery_time else "N/A"
        address_str = str(self.package_address_index) if self.package_address_index is not None else "N/A"
        return (f"Package ID: {self.package_id:3} | Address: {self.package_address:40} | Departed: {departure_str:5} -- Arrived: {delivery_str:5}")
        