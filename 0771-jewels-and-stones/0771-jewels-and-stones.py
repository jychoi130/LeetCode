import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:       
        stones_val = collections.Counter(stones)
        
        ans = 0
        for s in jewels:
            ans += stones_val[s]
            
        return ans
        