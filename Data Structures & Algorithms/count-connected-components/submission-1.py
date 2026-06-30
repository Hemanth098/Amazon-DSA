class Solution:
    from collections import defaultdict
    from typing import List
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = set()
        com = 0
        for i in range(n):
            if i not in vis:
                com+=1
                vis.add(i)

                que = [i]
                while que:
                    x = que.pop()
                    for j in adj[x]:
                        if j not in vis:
                            vis.add(j)
                            que = [j] + que
        return com

