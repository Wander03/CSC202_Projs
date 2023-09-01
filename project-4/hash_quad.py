from typing import List, Any, Optional

class HashTable:

    def __init__(self, table_size: int) -> None:            # can add additional attributes
        self.table_size = table_size                # initial table size
        self.hash_table: List = [None]*table_size   # hash table
        self.num_items = 0                          # empty hash table

    def __setitem__(self, key: str, item: Any) -> None:     # h[key] = value
        self.insert(key, item)

    def __getitem__(self, key: str) -> Any:                # h[key] -> value
        return self.get_value(key)

    def __contains__(self, key: str) -> bool:               # key in h -> T/F
        return self.in_table(key)

    def insert(self, key: str, value: Any) -> None:
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        h = self.horner_hash(key)

        i = 1
        added = False
        while not added:
            if self.hash_table[h] is None:
                self.hash_table[h] = (key, value)
                self.num_items += 1
                added = True
            elif self.hash_table[h] is not None and self.hash_table[h][0] == key:
                self.hash_table[h] = (key, value)
                added = True
            else:
                h = (h + i) % self.table_size
                i += 2

        if self.get_load_factor() > 0.5:
            self.num_items = 0
            self.table_size = self.table_size * 2 + 1
            old_table = self.hash_table
            self.hash_table = [None] * self.table_size
            for entry in old_table:
                if entry is not None:
                    self.insert(entry[0], entry[1])

    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        h = 0
        n = min(8, len(key))
        for i in range(n):
            h = (31 * h) + ord(key[i])

        return h % self.table_size

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        h = self.horner_hash(key)
        i = 1
        while True:
            if self.hash_table[h] is None:
                return False
            elif self.hash_table[h] is not None and self.hash_table[h][0] == key:
                return True
            
            h = (h + i) % self.table_size
            i += 2

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""
        h = self.horner_hash(key)
        i = 1
        while True:
            if self.hash_table[h] is None:
                return None
            elif self.hash_table[h] is not None and self.hash_table[h][0] == key:
                return h
            
            h = (h + i) % self.table_size
            i += 2

    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""
        keys = []
        for entry in self.hash_table:
            if entry is not None:
                keys.append(entry[0])
        
        return keys

    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        h = self.horner_hash(key)
        i = 1
        while True:
            if self.hash_table[h] is None:
                return None
            elif self.hash_table[h] is not None and self.hash_table[h][0] == key:
                return self.hash_table[h][1]
            
            h = (h + i) % self.table_size
            i += 2

    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

