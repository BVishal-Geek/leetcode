
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isImage(self, a, b) -> bool:
            if not a and not b: 
                return True
            if not a or not b: 
                return False
        
            return a.val==b.val and self.isImage(a.left, b.right) and self.isImage(a.right,b.left)

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root: 
            return True
        else: 
            return self.isImage(root.left, root.right)
        