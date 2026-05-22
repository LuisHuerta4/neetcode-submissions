class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        tracker = 1
        nums = sorted(list(set(nums)))
        print(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] + 1:
                tracker += 1 
            else:
                if tracker > res:
                    res = tracker
                tracker = 1
        if tracker > res:
            res = tracker
        return res