class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        if not fruits or not baskets: return -1

        n = len (fruits)
        if n != len(baskets): return -2

        tree = [0] * 4 * n
        self.buildSegTree(tree, baskets, 0, 0, n-1)
        unplaced = 0
        for fruit in fruits:
            if self.findBasket(tree, 0, 0, n-1, fruit) == False:
                unplaced += 1

        return unplaced

    def buildSegTree(self, tree: List[int], baskets: List[int], idx: int, low: int, high: int):
        if low == high:
            tree[idx] = baskets[low]
            return

        mid = (low + high) >> 1
        nextIdx = 2*idx + 1
        self.buildSegTree(tree, baskets, nextIdx, low, mid)
        self.buildSegTree(tree, baskets, nextIdx + 1, mid + 1, high)
        tree[idx] = tree[nextIdx + 1]
        if tree[idx] <  tree[nextIdx]:
            tree[idx] = tree[nextIdx]

    def findBasket(self, tree: List[int], idx: int, low: int, high: int, k: int):
        if tree[idx] < k:
            return False

        if low == high:
            tree[idx] = 0
            return True

        mid = (low + high) >>1
        nextIdx = (idx << 1) + 1
        found = True
        if tree[nextIdx] >= k:
            found = self.findBasket(tree, nextIdx, low, mid, k)
        else:
            found = self.findBasket(tree, nextIdx + 1, mid + 1, high, k)

        tree[idx] = tree[nextIdx + 1]
        if tree[idx] < tree[nextIdx]:
            tree[idx] = tree[nextIdx]

        return found
