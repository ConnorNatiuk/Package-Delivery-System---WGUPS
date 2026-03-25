class Hash_Table:

    """
    DESC: Initializes a hash table without using a built-in dictionary.
    """

    def __init__(self, capacity):
        """
        Initializes the hash table.
        
        Args:
            capacity (int): The number of buckets that will be inside of the hash table.
        """
        self.table = [[] for _ in range(capacity)]

    def _get_hash(self, key):
        """
        Returns a hash key based on the passed in integer and the length of the initialized structure. 
        """
        return int(key) % len(self.table)

    def insert(self, item_id, item_details):
        """
        Inserts data into the hash table based on the specific items id and the details of the item (usually in the form
        of an object such as a Package)
        """
        hash_key = self._get_hash(item_id) #Gets the hash key based on the value of the item_id
        bucket = self.table[hash_key] #Uses the hash key to determine which bucket the item will be placed in
        
        for i in range(len(bucket)): #Loops through the bucket to determine if the data is already in the specific bucket
            if bucket[i][0] == item_id:
                bucket[i][1] = item_details  ### THIS HANDLES COLLISIONS USING LINEAR PROBING ###
                return True 
        bucket.append([item_id, item_details]) #If the for loop ends, the data (item_id, item_details) was not found and is appended inside of that bucket.
        return True

    def lookup_data(self, item_id):
        """
        Returns item details of an object based on its ID, and returns None if the id isn't found.
        """
        hash_key = self._get_hash(item_id)  ##   This determines which bucket will be accessed
        bucket = self.table[hash_key]       ##

        for i in range(len(bucket)):
            if bucket[i][0] == item_id:
                return bucket[i][1] #Returns the object details if the bucket contains the items ID
        
        return None #If the object details aren't found inside of the bucket, the data is not in the hash table and the function returns None



