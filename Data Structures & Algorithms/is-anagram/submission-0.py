
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        has1 = {}
        has2 = {}
        for i in range(0,len(s)):
            has1[s[i]] = has1.get(s[i],0)+1
            has2[t[i]] = has2.get(t[i],0)+1
        return has1 == has2