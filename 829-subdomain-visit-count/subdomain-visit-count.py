from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = defaultdict(int)
        for s in cpdomains:
            c, dom = s.split()
            c = int(c)
            parts = dom.split(".")
            for i in range(len(parts)):
                cnt['.'.join(parts[i:])] += c
        return [f"{num} {domain}" for domain,num in cnt.items()]
