class TimeMap:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ''
        arr = self.d[key]
        # chr(127) (ASCII DEL) is greater than all printable characters 
        idx = bisect.bisect_right(arr, (timestamp, chr(127)))
        return arr[idx-1][1] if idx>0 else ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)