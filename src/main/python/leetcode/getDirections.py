class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        def findPath(root: TreeNode, target: int, path: List[str]) -> bool:
            if not root:
                return False
            if root.val == target:
                return True
            path.append('L')
            if findPath(root.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, target, path):
                return True
            path.pop()
            return False
        
        startPath, destPath = [], []
        findPath(root, startValue, startPath)
        findPath(root, destValue, destPath)

        # Find the common path length
        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1

        # Steps to go up from startValue to the common ancestor
        up_steps = 'U' * (len(startPath) - i)
        # Steps to go from the common ancestor to destValue
        remaining_steps = ''.join(destPath[i:])

        return up_steps + remaining_steps
