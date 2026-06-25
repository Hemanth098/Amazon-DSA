class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''x = 1
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
        return nums'''
        res = [1]*len(nums)
        pre = 1
        for i in range(0,len(nums)):
            res[i] = pre
            pre *= nums[i]
        suf = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suf
            suf *= nums[i]
        return res
        