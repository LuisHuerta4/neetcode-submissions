class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        solution = []
        lookup = {}

        for index, curr in enumerate(nums):
            if lookup.get(target - curr) == curr:
                solution.append(nums.index(target - curr))
                solution.append(index)
                return solution
            else:
                lookup[curr] = target - curr

        return solution