class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        solution = []
        mapping = dict()

        # create freq mapping
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1

        # sort dict values in desc order
        sorted_list = list(dict(sorted(mapping.items(), key=lambda item: item[1], reverse=True)).keys())
        solution = sorted_list[:k]

        return solution