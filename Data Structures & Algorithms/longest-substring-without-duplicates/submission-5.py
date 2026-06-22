class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        p = ""
        for i in range(0,len(s)):
            if s[i] in p :
                for k in range(0,len(p)):
                    if p[k] == s[i]:
                        p = p[k+1:]
                        break
                p = p+ s[i]
            else:
                p = p+ s[i]
            res = max(res,len(p))
        return res
            