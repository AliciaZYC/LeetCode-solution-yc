class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.valToIndex = {}
        self.rand = random.Random()

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False
        else:
            self.nums.append(val)
            self.valToIndex[val]=len(self.nums)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False
        else:
            index = self.valToIndex[val]
            last = self.nums[-1]
            self.nums[index] = last
            self.valToIndex[last] = index
            self.nums.pop()
            del self.valToIndex[val]
            return True

    def getRandom(self) -> int:
        return self.nums[self.rand.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()