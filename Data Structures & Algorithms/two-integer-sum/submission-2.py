class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store target - num in list. If target - num in list return those indexes.
        visited = []
        for i, num in enumerate(nums):
            if num in visited:
                return [nums.index(target - num), i]
            else:
                visited.append(target - num)
        return []