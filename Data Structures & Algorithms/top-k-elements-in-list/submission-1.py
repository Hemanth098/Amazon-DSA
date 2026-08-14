class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i in nums:
            if i not in x:
                x[i] = x.get(i,0)+1
            else:
                x[i]+=1
        sorted_data = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
        top_items = dict(list(sorted_data.items())[:k])
        return list(top_items.keys())
