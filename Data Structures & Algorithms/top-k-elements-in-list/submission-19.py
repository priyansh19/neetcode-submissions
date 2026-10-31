class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = dict()
        ls = []
        for num in nums:
            d1[num] = 1 + d1.get(num, 0)
        d2 = sorted(d1.items(), reverse=True)
        for i in range(0, k):
            ls.append(d2[i][0])
        return ls