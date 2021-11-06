class HashTable:
    class HashItem:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.capacity_level = 8
        self.size = 2**self.capacity_level-1
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def _hash(self, s):
        i = 1
        h = 0
        for ch in s:
            h += ord(ch) * i
            i += 1
        return h % self.size

    def put(self, key, value):
        i = HashTable.HashItem(key, value)
        h = self._hash(key)

        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size

        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = i

    def get(self, key):
        h = self._hash(key)

        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size

        return None
