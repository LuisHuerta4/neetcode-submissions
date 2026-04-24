class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = dict()
        for number in nums:
            if number not in tracker:
                tracker[number] = 1
            else:
                return True
        return False
