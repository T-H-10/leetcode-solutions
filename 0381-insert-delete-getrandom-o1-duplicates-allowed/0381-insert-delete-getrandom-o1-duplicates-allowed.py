from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.d = defaultdict(set) # key -> set(indices)
        self.arr = []

    def insert(self, val: int) -> bool:
        self.arr.append(val)
        self.d[val].add(len(self.arr) - 1)
        if len(self.d[val]) == 1:
            return True
        return False


    def remove(self, val: int) -> bool:
        if val not in self.d or not self.d[val]:
            return False

        i = self.d[val].pop()
        last_idx = len(self.arr) - 1
        last_val = self.arr[last_idx]

        if i != last_idx:
            self.arr[i] = last_val
            self.d[last_val].remove(last_idx)
            self.d[last_val].add(i)
        
        self.arr.pop()

        if not self.d[val]:
            del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()