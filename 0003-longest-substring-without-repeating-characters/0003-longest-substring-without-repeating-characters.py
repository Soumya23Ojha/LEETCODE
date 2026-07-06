class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        l, ans = 0, 0
        n = len(s)
        for r in range(n):
            cur = s[r]
            if cur in d and d[cur] >= l:
                l = d[cur] + 1
            d[cur] = r
            ans = max(ans, r-l+1)
        return ans