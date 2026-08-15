class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        is_swapped = False
        if self.nums == []:
            self.nums.append(val)
        if len(self.nums) == 1:
            if self.nums[0]> val:
                temp = self.nums[0]
                self.nums[0] = val
                self.nums.append(temp)
        else:
            for i in range(0,len(self.nums)-1):
                if self.nums[i+1]>val:
                    self.nums = self.nums[:i+1] + [val] +self.nums[i+1:]
                    is_swapped = True
                    break
            if not is_swapped:
                (self.nums).append(val)
        print(self.nums)
        return self.nums[len(self.nums)-self.k]

