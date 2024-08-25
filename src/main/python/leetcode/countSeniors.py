from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for str in details:
            age = str[-4:-2]
            if age > "60":
                count += 1

        return count
