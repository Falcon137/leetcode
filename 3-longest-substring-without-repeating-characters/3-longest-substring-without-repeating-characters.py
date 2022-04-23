class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        h = {}
        best = 0
        cur_start = 0
        cur = 0
        for idx,c in enumerate(s):
            if (c not in h) or (h[c] < cur_start):
                cur += 1
            else:
                cur_start = h[c]+1
                cur = idx-h[c]
            h[c] = idx
            best = max(best,cur)
        return best
                
