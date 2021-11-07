class HashTable:

    MAX_FILL_FACTOR = 0.6
    STARTING_CAPACITY = 2

    class HashItem:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.capacity_level = self.STARTING_CAPACITY
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

    def _grow(self):
        self.capacity_level += 1
        self.size = 2**self.capacity_level-1
        temp_slots = self.slots
        self.slots = [None for i in range(self.size)]
        for s in temp_slots:
            if s:
                self.slots[self._hash(s.key)] = s

    def get_load_factor(self):
        return self.count / self.size

    def put(self, key, value):
        i = HashTable.HashItem(key, value)
        h = self._hash(key)

        # IF THERE ISN'T ENOUGH ROOM, GROW BEFORE PUTTING
        # if self.get_load_factor() >= self.MAX_FILL_FACTOR:
        #     self._grow()

        starting_hash = h
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
            if h == starting_hash:
                raise RuntimeError("Cannot put into a full HashTable when using Linear Probing")

        if self.slots[h] is None:
            self.count += 1
            self.slots[h] = i

    def get(self, key):
        h = self._hash(key)

        starting_hash = h
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + 1) % self.size
            if h == starting_hash:  # LOOKED ALL THE WAY THROUGH A FULL TABLE.
                break

        raise KeyError(f"Key: '{key}' does not exist in HashTable.")
