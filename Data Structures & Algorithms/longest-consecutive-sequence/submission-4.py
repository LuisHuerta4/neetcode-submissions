class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            #Check if num is start of sequence (has no left value [num - 1])
            if num - 1 not in numSet:
                sequence = 0
                while num + sequence in numSet:
                    sequence += 1
                longest = max(sequence, longest)
        return longest