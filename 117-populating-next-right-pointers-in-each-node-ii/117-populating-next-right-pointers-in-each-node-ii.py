"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        dq = deque([root])
        while dq:
            size = len(dq)
            for i in range(size):
                n = dq.popleft()
                
                if n.left: dq.append(n.left)
                if n.right: dq.append(n.right)
                    
                if i != size - 1:
                    n.next = dq[0]
        
        return root
        