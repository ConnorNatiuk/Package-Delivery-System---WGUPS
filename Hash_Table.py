class Hash_Table:

    def __init__(self, capacity):
        self.table = [[] for _ in range(capacity)]

    def _get_hash(self, key):
        return int(key) % len(self.table)


    def insert(self, package_id, package_details):
        hash_key = self._get_hash(package_id)
        bucket = self.table[hash_key]
        
        for i in range(len(bucket)):
            if bucket[i][0] == package_id:
                bucket[i][1] = package_details
                return True
        bucket.append([package_id, package_details])
        return True

    def lookup_data(self, package_id):
        hash_key = self._get_hash(package_id)
        bucket = self.table[hash_key]

        for i in range(len(bucket)):
            if bucket[i][0] == package_id:
                return bucket[i][1]
        
        return None



