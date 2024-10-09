class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        balance = 0  # Unmatched '(' count
        insertions = 0  # Number of insertions needed

        for c in S:
            if c == '(':
                balance += 1
            else:  # c == ')'
                if balance > 0:
                    balance -= 1
                else:
                    insertions += 1  # Need an extra '('

        # Add remaining unmatched '('
        return insertions + balance
