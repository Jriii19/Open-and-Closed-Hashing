class OpenHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))
    
    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

class ClosedHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            while self.table[index] is not None:
                index = (index + 1) % self.size
            self.table[index] = (key, value)
    
    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                return v
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

# Contoh penggunaan OpenHashTable
open_table = OpenHashTable(10)
open_table.insert(5, "Nilai 5")
open_table.insert(15, "Nilai 15")
open_table.insert(25, "Nilai 25")

print(open_table.search(5))  # Output: Nilai 5
print(open_table.search(15)) # Output: Nilai 15
print(open_table.search(25)) # Output: Nilai 25

# Contoh penggunaan ClosedHashTable
closed_table = ClosedHashTable(10)
closed_table.insert(5, "Nilai 5")
closed_table.insert(15, "Nilai 15")
closed_table.insert(25, "Nilai 25")

print(closed_table.search(5))  # Output: Nilai 5
print(closed_table.search(15)) # Output: Nilai 15
print(closed_table.search(25)) # Output: Nilai 25
