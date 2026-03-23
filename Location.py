class Location:
    def __init__(self, location_id, location_name, location_address):
        self.location_id = location_id
        self.location_name = location_name
        self.location_address = location_address
    
    def __str__(self):
        return (f"ID: {self.location_id:3} | Name: {self.location_name:30} | Address: {self.location_address:30}")