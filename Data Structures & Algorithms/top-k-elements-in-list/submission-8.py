class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        for num in nums:
            d1[nums] = 1 + d1.get(nums, 0)
        return [d1.keys()]