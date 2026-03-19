class Hash_Table:

    def __init__(self, capacity):
        self.table = [[] for _ in range(capacity)]

    def _get_hash(self, key):
        return int(key) % len(self.table)

    def insert(self, item_id, item_details):
        hash_key = self._get_hash(item_id)
        bucket = self.table[hash_key]
        
        for i in range(len(bucket)):
            if bucket[i][0] == item_id:
                bucket[i][1] = item_details
                return True
        bucket.append([item_id, item_details])
        return True

    def lookup_data(self, item_id):
        hash_key = self._get_hash(item_id)
        bucket = self.table[hash_key]

        for i in range(len(bucket)):
            if bucket[i][0] == item_id:
                return bucket[i][1]
        
        return None



