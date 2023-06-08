import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.arrMap = {}

    def insert(self, val: int) -> bool:
        if val not in self.arr:
            self.arrMap[val] = len(self.arr)
            self.arr.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if not val in self.arrMap:
            return False
        
        last_element = self.arr[-1]
        index_remove = self.arrMap[val]

        self.arrMap[last_element] = index_remove
        self.arr[index_remove] = last_element
        
        self.arr[-1] = val
        self.arr.pop()

        self.arrMap.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()