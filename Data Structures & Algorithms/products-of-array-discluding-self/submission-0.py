class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    total *= nums[j]
            res.append(total)
            total = 1

        return res