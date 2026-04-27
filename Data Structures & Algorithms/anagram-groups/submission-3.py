class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ======== MY SOLUTION ========
        # groups = defaultdict(list)

        # for s in strs:
        #     key = tuple(sorted(s))
        #     groups[key].append(s)

        # return list(groups.values())

        # # ======== BEST SOLUTION ========
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())