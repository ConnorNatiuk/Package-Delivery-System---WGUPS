class Location:

    """
    DESC: Represents a location derived from the Locations.csv file in /Data
    """
    
    def __init__(self, location_id, location_name, location_address):
        
        """
        Initializes a new location instance.

        
        Args:
            location_id (int): The identification number for a location
            location_name (str): The name of the location
            location_address (str): The street address of the location
        """

        self.location_id = location_id
        self.location_name = location_name
        self.location_address = location_address
    
    def __str__(self):
        
        """
        Returns a formatted string with the location_id, location_name, and location_address.
        """

        return (f"ID: {self.location_id:3} | Name: {self.location_name:30} | Address: {self.location_address:30}")