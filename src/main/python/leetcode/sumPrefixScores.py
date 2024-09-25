from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # Number of times this prefix has been encountered

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        # Step 2: Build the Trie and count prefixes
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count += 1  # Increment count for this prefix

        # Step 3: Compute prefix scores for each word
        answer = []
        for word in words:
            node = root
            total = 0
            for ch in word:
                node = node.children[ch]
                total += node.count
            answer.append(total)
        
        return answer
