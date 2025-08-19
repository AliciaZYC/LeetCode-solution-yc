class HitCounter:

    def __init__(self):
        self.q = deque()
        self.WINDOW = 300
        

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        cutoff = timestamp - self.WINDOW
        while self.q and self.q[0] <= cutoff:
            self.q.popleft()
        return len(self.q)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)