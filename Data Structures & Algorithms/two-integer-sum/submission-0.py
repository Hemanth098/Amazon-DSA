class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        diff = 0
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in has:
                return [has[diff],i]
            has[nums[i]] = i
