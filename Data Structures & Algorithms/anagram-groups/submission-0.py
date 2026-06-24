class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 or len(strs) == 0:
            return [strs]
        res = []
        vis = {}
        for i in range(0,len(strs)-1):
            
            if i not in vis:
                
                x = [strs[i]]
                for j in range(i+1,len(strs)):
                    if len(strs[i]) == len(strs[j]):
                        if sorted(strs[i]) == sorted(strs[j]):
                            x.append(strs[j])
                            vis[j] = 1
                print(i)
                res.append(x)
        i+=1
        if i not in vis:
            res.append([strs[len(strs)-1]])
        return res