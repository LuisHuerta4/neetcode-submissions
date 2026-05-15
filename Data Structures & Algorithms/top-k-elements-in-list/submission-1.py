class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create frequency mapping
        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1

        # Create freq list where the index is the frequency
        # At each index store a list of numbers with the frequency of the index (freq of 5 is stored in index 5)
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in count_map.items():
            freq[count].append(num)

        # Look at K highest non-empty indexes in freq and add to solution
        solution = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                solution.append(j)
            if len(solution) == k:
                return solution
