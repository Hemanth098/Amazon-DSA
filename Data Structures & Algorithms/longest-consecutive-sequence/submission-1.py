class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums =list(set(nums))
        nums.sort()
        Curr_Count = 1
        Result = 1
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                Curr_Count+=1
            else:
                Result = max(Curr_Count,Result)
                Curr_Count = 1
        Result = max(Curr_Count,Result)
        return Result
            
