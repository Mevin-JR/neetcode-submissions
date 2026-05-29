class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for i in nums:
            hm[i] = hm.get(i, 0) + 1

        sorted_hm = dict(sorted(hm.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_hm.keys())[:k]