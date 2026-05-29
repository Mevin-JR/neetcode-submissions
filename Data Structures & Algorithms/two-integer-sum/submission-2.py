class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            req = target - v

            if req in seen:
                return [seen[req], i]

            seen[v] = i