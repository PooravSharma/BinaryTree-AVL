#Student ID: 10636908
#Name: Poorav Sharma 

"""code from Pearson Education, Inc p104 """
##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
##  AUTHOR: Original: J.V.     Edit: BcK
#Used to print the binary tree
def printTree(root, element="element", left="left", right="right"):                                
    def display(root, element=element, left=left, right=right):                                     
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, element)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, element)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, element)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    lines = []
    if root != None:
        lines, *_ = display(root, element, left, right)
    print("\t== Binary Tree: shape ==")
    print()
    if lines == []:
        print("\t  No tree found")
    for line in lines:
        print("\t", line)
    print()
###################################################

################  Classes and Methods  #################################
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True , current # Element is found

        return False
     # Find the depth of a given node in the BST
    def depth_nodeBST(self, N):
        current = self.root
        depth = 0
        while current != None:
            if N < current.element:
                current = current.left
                depth += 1
            elif N > current.element:
                current = current.right
                depth += 1
            else: # element matches current.element and return the depth of where it was found
                print("\nThe depth of node ",N," in the BTS is: ", depth)
                return  
                
                return 
        print("\nERROR: Node ", N, " not found in BST")
        return 
    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
                print("ERROR: node key ",e," already exists in the BST")#Lets the user know the key is already in a node in the BST
                return False # Duplicate node? not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)
    """
    # Return the size of the tree
    def getSize(self):
    
      return self.size"""
    #one prints all leaf nodes
    def leaf_BST(self):
        self.leaf_BSTHelper(self.root)
        
    def leaf_BSTHelper(self, r):
      if r != None:
        self.leaf_BSTHelper(r.left)       
        self.leaf_BSTHelper(r.right)
        if not r.left and not r.right:
            print(r.element, end = ", ")
            return

    #one prints all non_leaf nodes
    def non_leaf_BST(self):
        self.non_leaf_BSTHelper(self.root)
        
    def non_leaf_BSTHelper(self, r):
      if r != None:
        self.non_leaf_BSTHelper(r.left)       
        self.non_leaf_BSTHelper(r.right)
        if r.left or r.right:
            print(r.element, end = ", ")
            return
        
    # Inverse-Inorder traversal from the root
    def inverse_inorder(self):
      self.inverse_inorderHelper(self.root)

    # Inverse-Inorder traversal from a subtree
    def inverse_inorderHelper(self, r):
      if r != None:       
        self.inverse_inorderHelper(r.right)
        print(r.element, end = ", ")
        self.inverse_inorderHelper(r.left)
        
    
    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = ", ")
        self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = ", ")

    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = ", ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)

    # total subtree node count and all the subtree node of a specific node 
    def total_nodesBST(self, N):
        if self.search(N):
            root = self.search(N)[1]
            print("The nodes of subtree ", N, ": \n")
            nodeCount = self.total_nodesBSTHelper(root)
            print("\nTotal number of node: ", nodeCount)
            
        else:
            print("\nERROR: Node ", N ," not found!")
    # total subtree node count and all the subtree node of a specific node 
    def total_nodesBSTHelper(self, root):
        nodeCount = 0
        if root != None:
            nodeCount += 1
            print(root.element, end = " ")
            nodeCount +=self.total_nodesBSTHelper(root.left)
            nodeCount +=self.total_nodesBSTHelper(root.right)
        return nodeCount
    # Finding the depth of the subtree using Postorder traversal
    def depth_subtreeBST(self, N):
      if self.search(N):
        root = self.search(N)[1]            
        depth = self.depth_subtreeBSTHelper(root)-1#to make it start from 0
        print("\nThe depth of subtree rooted at node ", N, " is: ",depth)            
      else:
        print("\nERROR: Subtree rooted at node ", N ," not found!")

    # Finding the depth of the subtree using Postorder traversal
    def depth_subtreeBSTHelper(self, root):
        depth = 0    
        if root != None:
            leftDepth = self.depth_subtreeBSTHelper(root.left)
            rightDepth = self.depth_subtreeBSTHelper(root.right)
            depth = max(leftDepth, rightDepth)+1       
        
        return depth 
    #Delete a node from the tree
    def delete_(self, key):
        
        if self.search(key):
            root = self.search(key)[1]
            self.delete_Helper(self.root, key)
            return True, root
        else:
           print("\nERROR: Node", key ," not found!")
           return False, key   
    def delete_Helper(self, root,  key):

        if root is None:
            return root

        if key < root.element:
            root.left = self.delete_Helper(root.left, key)
        elif key > root.element:
            root.right = self.delete_Helper(root.right, key)
        else:
            # Case 1: Node to be deleted is a leaf node (has no children)
            if root.left is None and root.right is None:
                return None

            # Case 2: Node to be deleted has only one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = self.findSuc(root.right)
            root.element = successor.element
            root.right = self.delete_Helper(root.right, successor.element)
            
        return root

    def findSuc(self, node):
        currentRoot = node
        while currentRoot.left is not None:
            currentRoot = currentRoot.left
        return currentRoot

    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root == None
      self.size == 0

    # Return the root of the tree
    def getRoot(self):
      return self.root

class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None

#############################################
outputdebug = True 

def debug(msg):
    if outputdebug:
        print (msg)
        
class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 

class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 
        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 


    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level=0, pref=''):
        '''
        Display the whole tree (but turned 90 degrees counter-clockwisely). Uses recursive def.
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()  
        if(self.node != None): 
            if self.node.left != None:
                self.node.right.display(level + 2, '>')
            print (' ' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')    
            if self.node.left != None: 
                self.node.left.display(level + 2, '<')
    def getNode(self):
        return self.node
      
#############################################
#method displays the options that the user can pick from    
def optionDisplay(displayNumber):     
    if displayNumber == 1:
        print("\nQuestion 3: AVL tree: deleting a node\n")
        print("\n1. Pre-load a sequence of integers to build a AVL tree \n")
        print("2. Manually enter integer values/keys, one by one, to build an AVL tree\n")
        print("3. Exit\n")
    elif displayNumber == 2:
        print("\n\nQuestion 3: AVL tree: deleting a node\n")
        print("1. Display the AVL tree, showing the height and balance factor for each node.\n")
        print("2. Print the pre-order, in-order, and post-order traversal sequences of the AVL tree\n")
        print("3. Print all leaf nodes of the AVL tree, and all non-leaf nodes (separately)\n")
        print("4. Insert a new integer key into the AVL tree\n")
        print("5. Delete an integer key from the AVL tree\n")
        print("6. Exit\n")
       
 
        
#this method accepts only valid integer which can be used choose an option  
def optionInput(max, min, displayNumber):
    optionDisplay(displayNumber)
    while True:
        optionNumber = input("\nEnter number to choose option: ")
        if optionNumber.isnumeric() and max > int(optionNumber) > min:
            optionNumber = int(optionNumber)
            break
        else:
            print("\nError!!! Invalid Input \nPlease insert correct option number\n")
            optionDisplay(displayNumber)
    return optionNumber


#this method deals with the first menu option that the users has chosen    
def menuOneOption(optionNumber):
    if optionNumber == 1:
        menuOneOptionOne()
    elif optionNumber == 2:
        menuOneOptionTwo()
    else:
        print("\nExiting\n")
        exit()
        
#this method deals with the first menu option that the users has chosen
def menuTwoOption(sequence):
    bTree = BinaryTree()
    inputtoTree(bTree, sequence)
    aTree = AVLTree()    
    inputtoTree(aTree, sequence)
    
    while True:
        optionNumber = optionInput(7, 0, 2)
        if optionNumber == 1:
            menuTwoOptionOne(aTree)
        elif optionNumber == 2:
            menuTwoOptionTwo(bTree)
        elif optionNumber == 3:
            menuTwoOptionThree(bTree)
        elif optionNumber == 4:
            menuTwoOptionFour(bTree)
        elif optionNumber == 5:
            menuTwoOptionFive(bTree)          
        else:
            break
        
        
#first option us the pre loaded sequence. it will be sorted and displayed as a balanced binary tree
def menuOneOptionOne():
    #the sequence below was required to be tested
     preSequence = [58, 82, -55, 20, 35, 79, 23, 14, 0, -21, 103, 92, 44, 84, 50, 46, 47, 49, 45, 72, 89]

    #use this sequence below if you want to test another sequence
    #preSequence = [-2, 17, 94, -55, 36, -9, 12, -83, 68, 7, -76, 45, -30, 59, 0, -42, 81, -98, 23]
     
     menuTwoOption(preSequence)

        
#second option will ask for u to add integer into the sequence. the sequence will be sorted and displayed as a balanced binary tree
def menuOneOptionTwo():
     userSequence = inputInteger()         
     menuTwoOption(userSequence)
     
     
#askes for integer input. it makes sure it gets all integer value and it is not repeated.
def inputInteger():
    userInput = []
    while True:
        number = input("\nEnter an integer ('x' to finish): ")
        if number == 'x' and len(userInput) ==0:
            print("\nYou need to input at least one integer before finishing.")
        elif number == 'x':
            break
        else:
            try:
                number = int(number)
                if number in userInput:
                    print("\nThat integer is already in the sequence enter a different integer.")
                else:
                    userInput.append(number)
            except ValueError:
                print("Invalid input!!! Please enter a valid integer or 'x' to finish.")
    return userInput

def inputtoTree(Tree, sequence):    
    for element in sequence:
        Tree.insert(element)
    return

def menuTwoOptionOne(bTree):
     printTree(bTree.getNode())
     
     
     
def menuTwoOptionTwo(bTree):
    print("\nPre-Order Traversal:\n")
    bTree.preorder()
    print("\n\nIn-Order Traversal:\n")
    bTree.inorder()
    print("\n\nPost-Order Traversal:\n")
    bTree.postorder()
    print("\n\nInverse-In-Order Traversal:\n")
    bTree.inverse_inorder() 
     
def menuTwoOptionThree(bTree):
    print("\nAll Leaf nodes:\n")
    bTree.leaf_BST()
    print("\n\nAll Non-leaf nodes:\n")
    bTree.non_leaf_BST()
     

def menuTwoOptionFour(bTree):
    try:
         number = input("Enter a integer: ")
         number = int(number)
         inserted = bTree.insert(number)
    except ValueError:
         print("Invalid input!!! Please enter a valid integer")
    if inserted ==True:
        print("\nInteger", number, "has been inserted into the BST")
        print("\n\nInverse-In-Order Traversal:\n")
        bTree.inverse_inorder()
    

def menuTwoOptionFive(bTree):
    try:
         number = input("Enter a integer: ")
         number = int(number)
         deleted = bTree.delete_(number)[0]
    except ValueError:
         print("Invalid input!!! Please enter a valid integer")
    if deleted == True:
        print("\nInteger", number, "has been deleted into the BST")
        print("\n\nInverse-In-Order Traversal:\n")
        bTree.inverse_inorder()
     
    

#####################################################################
      
####################### Main Code ###################################
    
looping = True
while looping == True:    
    menuOneOption(optionInput(4,0,1))
