class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.allTokens = dict()
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.allTokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.allTokens and self.allTokens[tokenId] > currentTime:
            self.allTokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for tk in self.allTokens.values():
            if tk > currentTime:
                cnt += 1
        return cnt
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)