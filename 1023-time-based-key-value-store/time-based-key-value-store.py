class TimeMap:

    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_time_map:
            self.key_time_map[key] = SortedDict()
        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_time_map:
            return ""
        it = self.key_time_map[key].bisect_right(timestamp)
        if it == 0:
            return ""
        return self.key_time_map[key].peekitem(it -1)[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)