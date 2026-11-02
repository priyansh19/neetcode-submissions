class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket_key = key % self.size
        if key not in self.bucket[bucket_key]:
            self.bucket[bucket_key].append(key) 

    def remove(self, key: int) -> None:
        bucket_key = key % self.size
        if key in self.bucket[bucket_key]:
            self.bucket[bucket_key].remove(key)
        
    def contains(self, key: int) -> bool:
        bucket_key = key % self.size
        return key in self.bucket[bucket_key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)