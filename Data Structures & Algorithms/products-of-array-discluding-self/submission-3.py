class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        y = 0
        for i in nums:
            if i!=0:
                x = x*i
            else:
                y +=1
        print(y)
        if y == len(nums):
            x = 0
        
        for i in range(0,len(nums)):
            if nums[i]==0:
                if y >1:
                    nums[i] = 0
                else:
                    nums[i] = x
            else:
                if y!=0:
                    nums[i] = 0
                else:
                    nums[i] = x//nums[i]
        return nums
        