class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        top = -1
        for i in range(0,len(s)):
            if s[i]== '{' or s[i]== '[' or s[i] == '(' :
                q.append(s[i])
                top += 1
            elif top == -1:
                return False
            elif s[i] == '}':
                if q[top] == '{' and top!=-1 :
                    q.pop()
                    top-=1
                else:
                    return False
            elif s[i] == ']':
                if q[top] == '[' and top!=-1:
                    q.pop()
                    top -= 1
                else:
                    return False
            elif s[i] == ')':
                if q[top] == '('and top!=-1:
                    q.pop()
                    top -= 1
                else:
                    return False
        if top!=-1:
            return False
        return True