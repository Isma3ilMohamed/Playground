from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # Early reject: result must be at least as long as the longest word,
        # and at most one digit longer (for a final carry).
        maxw = max(map(len, words))
        if not (maxw <= len(result) <= maxw + 1):
            return False

        # Reverse for LSD → MSD traversal
        rwords = [w[::-1] for w in words]
        rres   = result[::-1]
        max_len = len(rres)

        # Collect letters; quick reject if >10
        letters = set(''.join(words) + result)
        if len(letters) > 10:
            return False

        # Leading chars cannot be zero
        leading = {w[0] for w in words if len(w) > 1}
        if len(result) > 1:
            leading.add(result[0])

        assign = {}           # char → digit
        used   = [False]*10   # digit used flag

        W = len(rwords)
        R = rres

        def dfs(col: int, row: int, carry: int) -> bool:
            # If we've finished all columns...
            if col == max_len:
                # no leftover carry
                return carry == 0

            # If we're still summing across the words in this column
            if row < W:
                w = rwords[row]
                if col >= len(w):
                    # this word has no digit here → skip to next row
                    return dfs(col, row+1, carry)

                ch = w[col]
                if ch in assign:
                    return dfs(col, row+1, carry + assign[ch])

                # try assigning any unused digit
                for d in range(10):
                    if used[d]: 
                        continue
                    if d == 0 and ch in leading:
                        continue
                    assign[ch] = d
                    used[d] = True
                    if dfs(col, row+1, carry + d):
                        return True
                    # backtrack
                    used[d] = False
                    del assign[ch]
                return False

            # We've summed all words for this column; now handle the result digit
            total = carry
            ch = R[col]
            want = total % 10
            new_carry = total // 10

            if ch in assign:
                if assign[ch] != want:
                    return False
                return dfs(col+1, 0, new_carry)

            # assign result letter
            if used[want] or (want == 0 and ch in leading):
                return False
            assign[ch] = want
            used[want] = True
            ok = dfs(col+1, 0, new_carry)
            if ok:
                return True
            # backtrack
            used[want] = False
            del assign[ch]
            return False

        return dfs(0, 0, 0)
