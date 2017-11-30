"""Hash table in python."""


class HashTable:
    """Hash table use str for keys, val can be anything."""

    def __init__(self, bucket_count=100):
        """Init an instance of Hash Table."""
        self.bucket_count = bucket_count
        self.size = 0
        self.data = [[] for _ in range(bucket_count)]

    def set(self, key, val):
        """Insert key val pair to the hash table."""
        if not isinstance(key, str):
            raise ValueError('key can only be string')
        found_cell, bucket = self._find_by_key(key)
        self._set_helper(found_cell, bucket, key, val)

    def get(self, key):
        """Get the value for the given key."""
        found_cell, bucket = self._find_by_key(key)
        return self._get_helper(found_cell, key)

    def _find_by_key(self, key):
        """Find val, bucket from key in current table."""
        index = self._additive_hash(key)
        bucket = self.data[index]  # Corresponding bucket from hashed result
        found_cell = None
        for item in bucket:
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

    def _get_helper(self, found_cell, key):
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
        return self.additive_hash(key)

    def _djb2_hash(self, key_str):
        """Hashing algorithm created by Dan Bernstein."""
        h = 6820  # any large int
        for char in key_str:
            h += ((h << 1) * 33) + ord(char)
        return h % self.bucket_count

    def _hash_djb2(self, key):
        """Hash the key with djb2 hashing."""
        return self._djb2_hash(key)

    def __repr__(self):
        """Repr fun."""
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self._keys]) + ' }'

# if __name__ == "__main__":

