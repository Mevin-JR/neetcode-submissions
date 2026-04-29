import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prefix = nums[:i]
            suffix = nums[i + 1:]

            result.append(math.prod(prefix + suffix))

        return result