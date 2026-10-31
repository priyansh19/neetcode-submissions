class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if dict1.get(diff):
                return [i,dict1[diff]]
            else:
                dict1[nums[i]] = i
        return [-1,-1]