class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        best = 0
        for v in prices:
            cand = v-cur_min
            best = max(best,cand)
            cur_min = min(v,cur_min)
        return best
        
        