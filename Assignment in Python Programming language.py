
# binary tree node 
class Node: 
    # Constructor to create new node 
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None
  
  
# This function returns pointer to LCA of  
# two given values n1 and n2. 
def LCA(root, n1, n2): 
      
    # Base case 
    if root is None: 
        return None
  
    # If either n1 or n2 matches with root's 
    # key, report the presence by returning 
    # root  
    if root.data == n1 or root.data == n2: 
        return root 
  
    # Look for keys in left and right subtrees 
    left = LCA(root.left, n1, n2) 
    right = LCA(root.right, n1, n2) 
  
    if left is not None and right is not None: 
        return root 
  
    # Otherwise check if left subtree or  
    # right subtree is LCA 
    if left: 
        return left 
    else: 
        return right 
  
  
# function to find distance of any node 
# from root 
def findLevel(root, data, d, level): 
      
    # Base case when tree is empty 
    if root is None: 
        return
  
    # Node is found then append level 
    # value to list and return 
    if root.data == data: 
        d.append(level) 
        return
  
    findLevel(root.left, data, d, level + 1) 
    findLevel(root.right, data, d, level + 1) 
  
# function to find distance between two 
# nodes in a binary tree 
def findDistance(root, n1, n2): 
      
    lca = LCA(root, n1, n2) 
      
    # to store distance of n1 from lca 
    d1 = []  
      
    # to store distance of n2 from lca 
    d2 = []  
  
    # if lca exist 
    if lca: 
          
        # distance of n1 from lca 
        findLevel(lca, n1, d1, 0)  
          
        # distance of n2 from lca 
        findLevel(lca, n2, d2, 0)  
        return d1[0] + d2[0] 
    else: 
        return -1
  
  
# Driver Code to test above functions 
root = Node(5) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(1) 
root.right.left = Node(9) 
root.right.right = Node(6) 
root.right.left.right = Node(4) 
  
print("Dist(7,1) = ", findDistance(root, 7, 1))
  
print("Dist(9,6) = ", findDistance(root, 9, 6))

print("Dist(2,3) = ", findDistance(root, 2, 3))

# Position count

Str1 = """ 
        counting the position where the node is not present at node value two
        counting the position where the node is not present at node value seven
        counting the position where the node is not present at node value three
        counting the position where the node is not present at node value nine
        """ .count('position')

print('counting the total positions where the node is not present = ', Str1)
