class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        newNums = [1] * l 
        for i in range(l):
            p = 1
            for j in range(l):
                if i != j:
                    p *= nums[j]
                newNums[i] = p
        return newNums

## [1,2,4,6] - brute force version