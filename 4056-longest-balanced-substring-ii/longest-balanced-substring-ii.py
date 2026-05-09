class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        # Build prefix sum array: p[i] = [count_a, count_b, count_c] for s[0:i]
        # p[0] = [0,0,0] represents empty prefix
        p = [[0,0,0]]
        for c in s:
            p.append(p[-1][:])  # Copy previous counts
            p[-1]["abc".index(c)] += 1  # Increment count for current character
        
        ans = 0
        m = {}  # Map: (key_pattern) -> earliest index where this pattern occurs
        
        # Iterate through all prefix positions
        for i, (a,b,c) in enumerate(p):
            # Key insight: For a substring to be balanced, the differences between 
            # character counts must remain constant. We track 7 different patterns
            # representing different combinations of character presence.
            for k in [
                (-1,a-b,a-c),  # Pattern 1: all three chars present, a-b and a-c constant
                (-2,a-b,c),    # Pattern 2: a and b present, c count tracked separately
                (-3,b-c,a),    # Pattern 3: b and c present, a count tracked separately
                (-4,c-a,b),    # Pattern 4: c and a present, b count tracked separately
                (-5,b,c),      # Pattern 5: only b and c present
                (-6,c,a),      # Pattern 6: only c and a present
                (-7,a,b),      # Pattern 7: only a and b present
            ]:
                # Store the first occurrence of each pattern
                if k not in m:
                    m[k] = i
                else:
                    # If we've seen this pattern before, the substring between
                    # those indices has constant differences = balanced substring
                    ans = max(ans, i - m[k])
        
        return ans