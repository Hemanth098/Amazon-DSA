class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = ""
        for i in range(0,len(s)):
            if s[i].isalpha() or s[i].isdigit():
                q += s[i]
        q = q.lower()
        print(q)
        if q == q[::-1]:
            return True
        return False
