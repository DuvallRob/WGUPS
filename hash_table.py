# hash_table.py

class HashTable:
    def __init__(self):
        self.table = [None] * 100  # Example size, can be adjusted
    
    def _hash(self, key):
        return int(key) % len(self.table)
    
    def insert(self, key, item):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append(item)
    
    def lookup(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item['Package ID'] == key:
                    return item
        return None
