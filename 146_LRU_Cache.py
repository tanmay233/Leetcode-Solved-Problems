class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict[key] = self.dict.pop(key)
        return self.dict[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.capacity:
                self.capacity -= 1
            else:
                self.dict.pop(next(iter(self.dict)))

        self.dict[key] = value
