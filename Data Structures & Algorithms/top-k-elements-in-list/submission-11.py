class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = dict()
        for num in nums:
            d1[num] = 1 + d1.get(num, 0)
        print(d1)
        return 0