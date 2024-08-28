                            
#Ascending order of x for the verticals ---- L TO R 
#And for the level ascedning order of level |

#So basically for every vertical we need to iterate on the level

#So going to every node and assigning level and vertical - striver is doing level order.

#We have a queue where we will store the node , vertical and the level

#Taking a map which will carry Integer (Vertical) and within it A MAP FOR THE LEVELS(SORTED ORDER) MULTISET IN CPP,

#So first vertical 0 and level 0 is (1,0,0 is inserted) into queue - NOW POP IT AND STORE IT IN UR DATA STRUCTURE.
#So now in the queue (since we are doing level order traversal) we will add (2,-1,1) and (3,1,1)
# Now for the next iteration get node = 2 from the queue (pop it) - store it in the data structure, Next we add(4,-2,2) (10,0,2)
#Now for the next iteration get node = 3 from the queue (pop it) - store it in the data structure , Next we add (9,0,2) (10,2,2)

#The main idea is if ur moving left move the vertical by -1 and level by +1
#If ur moving right move the vertical by +1 and level by +1

#I THINK WE ARE DOING PREORDER TRAVERSAL HERE.

from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes = defaultdict(lambda: defaultdict(list))
        q = deque([(root, 0, 0)])      
        
        while q:
            node, x, y = q.popleft()
            nodes[x][y].append(node.val)

            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))

        res = []
        for x in sorted(nodes):
            col = []
            for y in sorted(nodes[x]):
                col.extend(sorted(nodes[x][y]))
            res.append(col)
                
        return res  