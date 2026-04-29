import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            pre = nums[:i]
            suf = nums[i + 1:]

            result.append(math.prod(pre + suf))

        return result