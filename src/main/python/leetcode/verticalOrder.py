# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        mp=defaultdict(list)
        mincol=0
        maxcol=0
        q=deque([(root,0)]) 
        while q:
            node,pos=q.popleft()
            mp[pos].append(node.val)
            mincol=min(mincol,pos)
            maxcol=max(maxcol,pos)
            if node.left:
                q.append((node.left,pos-1))
            if node.right:
                q.append((node.right,pos+1))
        
        res=[]
        for i in range(mincol,maxcol+1):
            res.append(mp[i])
        return res
