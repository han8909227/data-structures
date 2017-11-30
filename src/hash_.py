"""Hash table in python."""


class HashTable:
    """Hash table use str for keys, val can be anything."""

    def __init__(self, bucket_count=100):
        """Init an instance of Hash Table."""
        self.bucket_count = int(bucket_count)  # must be whole num
        self.size = 0
        self.data = [[] for _ in range(self.bucket_count)]
        self.keys = []

    def set(self, key, val):
        """Insert key val pair to the hash table."""
        if not isinstance(key, str):
            raise ValueError('key can only be string')
        found_cell, bucket = self._find_by_key(key)
        self._set_helper(found_cell, bucket, key, val)

    def get(self, key):
        """Get the value for the given key."""
        if not isinstance(key, str):
            raise ValueError('key can only be string')
        found_cell, bucket = self._find_by_key(key)
        return self._get_helper(found_cell)

    def _find_by_key(self, key):
        """Find val, bucket from key in current table."""
        index = self._additive_hash(key)
        bucket = self.data[index]  # Corresponding bucket from hashed result
        found_cell = None
        for item in bucket:  # find cell by loop through bucket
            if item[0] == key:
                found_cell = item
                break
        return (found_cell, bucket)

    def _set_helper(self, found_cell, bucket, key, val):
        """Append to the proper bucket determined by hash fun."""
        if found_cell:
            found_cell[1] = val
        else:
            bucket.append([key, val])  # append a new cell
            self.size += 1
            self.keys.append(key)

    def _get_helper(self, found_cell):
        """Get helper fun."""
        if found_cell:  # if cell is found (not none)
            return found_cell[1]
        else:
            raise KeyError('no such key exist in this hash table')

    def _additive_hash(self, key_str):
        """Additive hash fun."""
        return sum([ord(c) for c in key_str]) % self.bucket_count

    def _hash(self, key):
        """Hash the key with additive hashing."""
        return self._additive_hash(key)

    def _djb2_hash(self, key_str):
        """Hashing algorithm created by Dan Bernstein."""
        h = 682034123453423  # any large int
        for char in key_str:
            h = ((h << 1) * 33) + ord(char)
        return h % self.bucket_count

    def _hash_jsw(self, key_str):
        """Basic JSW hasing."""
        h = 59207892748932
        for char in key_str:
            h = ((h << 1 | h >> 31 & 0xffffffff) ^ ord(char))  # retain 32 bits with hex decimal constant
        return h % self.bucket_count

    def __repr__(self):
        """Repr fun."""
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self.keys]) + ' }'

if __name__ == "__main__":
    a = HashTable()  # create ht size 100
    a.set('t', 1)
    a.set('te', 10)
    a.set('tes', 100)
    a.set('test', 1000)

