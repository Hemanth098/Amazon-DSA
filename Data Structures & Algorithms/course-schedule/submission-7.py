from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        wanted = defaultdict(list)
        for pre,order in prerequisites:
            wanted[order].append(pre)
        state = [0]*numCourses
        def has_cycle(cun):
            if state[cun] == 1:
                return True
            if state[cun] == 2:
                return False
            state[cun] = 1

            for curr in wanted[cun]:
                if has_cycle(curr):
                    return True
            state[cun] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True