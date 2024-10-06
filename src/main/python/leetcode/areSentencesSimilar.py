class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        left = 0
        right1 = len(words1) - 1
        right2 = len(words2) - 1

        # Match words from the start
        while left <= right1 and left <= right2 and words1[left] == words2[left]:
            left += 1

        # Match words from the end
        while right1 >= left and right2 >= left and words1[right1] == words2[right2]:
            right1 -= 1
            right2 -= 1

        # Check if all words have been matched or unmatched words are contiguous
        return left > right1 or left > right2
