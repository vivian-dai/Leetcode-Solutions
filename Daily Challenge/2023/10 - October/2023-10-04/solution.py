class MyHashMap:

    def __init__(self):
        self.lst = []
        for i in range(1000001):
            self.lst.append(-1)

    def put(self, key: int, value: int) -> None:
        self.lst[key] = value

    def get(self, key: int) -> int:
        return self.lst[key]


    def remove(self, key: int) -> None:
        self.lst[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
