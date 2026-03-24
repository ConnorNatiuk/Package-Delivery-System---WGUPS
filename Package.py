class Package:

    """
    DESC: Represents a package object that contains all information for packages from Data/Packages.csv,
    captures the package address index and time information regarding the departure and delivery of each package
    """

    def __init__(self, package_id, package_address, package_city, package_state,
                 package_zip, package_deadline, package_weight, special_notes, delivery_status):
        
        """
        Attributes:
            package_id (int): The identification number of the package
            package_address (str): The street address for delivery
            package_city (str): The address city
            package_state (str): The address state
            package_zip (str): The zip code for the address
            package_deadline (str): The time by which the package must be delivered.
            package_weight (float): Weight of the package
            special_notes (str): Special notes regarding certain constraints on each package
            delivery_status (str): Current delivery status
            package_address_index (int): The corresponding index in the distance list
            departure_time (datetime): The time the truck left the hub with this package
            delivery_time (datetime): The time the package was delivered
        """

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
        
        """
        Returns a formatted string with the package ID, address, departure time, and arrival time (delivery time).
        """

        departure_str = self.departure_time.strftime("%H:%M") if self.departure_time else "N/A"
        delivery_str = self.delivery_time.strftime("%H:%M") if self.delivery_time else "N/A"
        address_str = str(self.package_address_index) if self.package_address_index is not None else "N/A"
        return (f"Package ID: {self.package_id:3} | Address: {self.package_address:40} | Departed: {departure_str:5} -- Arrived: {delivery_str:5}")
        