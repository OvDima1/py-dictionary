from typing import Any, Hashable


class Dictionary:
    load_factor = 2 / 3

    def __init__(self) -> None:
        self.capacity = 8
        self.length = 0
        self.threshold = int(self.capacity * self.load_factor)
        self.hash_table = self.create_hash_table()

    def create_hash_table(self) -> list:
        return [[] for _ in range(self.capacity)]

    def resize(self) -> None:
        hash_table = self.hash_table
        self.length = 0
        self.capacity *= 2
        self.threshold = int(self.capacity * self.load_factor)
        self.hash_table = self.create_hash_table()

        for element in hash_table:
            if element:
                self.__setitem__(element[0], element[2])

    def __getitem__(self, key: Hashable) -> Any:
        hash_key = hash(key)
        hash_index = hash_key % self.capacity

        while self.hash_table[hash_index]:
            if self.hash_table[hash_index][0] == key:
                return self.hash_table[hash_index][2]
            hash_index = (hash_index + 1) % self.capacity
        raise KeyError

    def __setitem__(self, key: Hashable, item: Any) -> None:
        if self.length == self.threshold:
            self.resize()
        hash_key = hash(key)
        hash_index = hash_key % self.capacity

        while True:
            if not self.hash_table[hash_index]:
                self.hash_table[hash_index] = [key, hash_key, item]
                self.length += 1
                break
            elif self.hash_table[hash_index][0] == key:
                self.hash_table[hash_index][2] = item
                break
            hash_index = (hash_index + 1) % self.capacity

    def __len__(self) -> int:
        return self.length
