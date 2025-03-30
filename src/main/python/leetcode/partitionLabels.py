class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}
        result = []

        for i, ele in enumerate(s):
            hmap[ele] = i

        cur = 0
        ans = -1
        for i, ele in enumerate(s):
            cur += 1
            if hmap[ele] > ans:
                ans = hmap[ele]

            if i == ans:
                result.append(cur)
                cur = 0

        return result
