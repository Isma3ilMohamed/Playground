class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        mx = max(potions)
        cnt = [0] * (mx + 1)
        for y in potions:
            cnt[y] += 1  

        for i in range(mx - 1, -1, -1):
            cnt[i] += cnt[i + 1]

        for i, x in enumerate(spells):
            low = (success - 1) // x + 1
            spells[i] = cnt[low] if low <= mx else 0
        return spells
