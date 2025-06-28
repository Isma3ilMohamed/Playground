class Solution:
    def maxSubsequence(self, a: List[int], k: int) -> List[int]:
        return [v for _, v in sorted(nlargest(k, enumerate(a), itemgetter(1)))]
