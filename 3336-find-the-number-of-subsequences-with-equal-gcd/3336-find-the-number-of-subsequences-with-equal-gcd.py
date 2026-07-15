import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        dp = {(0, 0): 1}
        
        for x in nums:
            next_dp = {}
            
            for (g1, g2), count in dp.items():
                next_dp[(g1, g2)] = (next_dp.get((g1, g2), 0) + count) % MOD
                
                new_g1 = math.gcd(g1, x)
                next_dp[(new_g1, g2)] = (next_dp.get((new_g1, g2), 0) + count) % MOD
                
                new_g2 = math.gcd(g2, x)
                next_dp[(g1, new_g2)] = (next_dp.get((g1, new_g2), 0) + count) % MOD
            
            dp = next_dp
        
        ans = 0
        
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + count) % MOD
        
        return ans