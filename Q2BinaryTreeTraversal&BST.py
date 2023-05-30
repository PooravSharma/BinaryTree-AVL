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
#method displays the options that the user can pick from    
def optionDisplay(displayNumber):     
    if displayNumber == 1:
        print("\nQuestion 2: Application to binary tree traversal & BST\n")
        print("\n1. Pre-load a sequence of integers to build a BST \n")
        print("2. Manually enter integer values, one by one, to build a BST\n")
        print("3. Exit\n")
    elif displayNumber == 2:
        print("\n\n\nQuestion 2: Application to binary tree traversal & BST\n")
        print("1. Display the tree shape of current BST, and then show the pre-order, in-order, post-order and inverse-in-order traversal sequences of the BST\n")
        print("2. Show all leaf nodes of the BST, and all non-leaf nodes (separately)\n")
        print("3. Show a sub-tree and count its nodes\n")
        print("4. Show the depth of a given node in the BST\n")
        print("5. Show the depth of a subtree of the BST\n")
        print("6. Insert a new integer key into the BST\n")
        print("7. Delete an integer key from the BST\n")
        print("8. Exit\n")
 
        
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
    while True:
        optionNumber = optionInput(9, 0, 2)
        if optionNumber == 1:
            menuTwoOptionOne(bTree)
        elif optionNumber == 2:
            menuTwoOptionTwo(bTree)
        elif optionNumber == 3:
            menuTwoOptionThree(bTree)
        elif optionNumber == 4:
            menuTwoOptionFour(bTree)
        elif optionNumber == 5:
            menuTwoOptionFive(bTree)
        elif optionNumber == 6:
            menuTwoOptionSix(bTree)
        elif optionNumber == 7:
            menuTwoOptionSeven(bTree)          
        else:
            break
        
        
#first option us the pre loaded sequence. it will be sorted and displayed as a balanced binary tree
def menuOneOptionOne():
    #the sequence below was required to be tested
     preSequence = [58, 84, 68, 23, 38, 82, 26, 17, 24, 106, 95, 48, 88, 54, 50, 51, 53, 49, -6, -46]

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

def inputtoTree(bTree, sequence):    
    for element in sequence:
        bTree.insert(element)
    return

def menuTwoOptionOne(bTree):
     printTree(bTree.getRoot())
     
     print("\nPre-Order Traversal:\n")
     bTree.preorder()
     print("\n\nIn-Order Traversal:\n")
     bTree.inorder()
     print("\n\nPost-Order Traversal:\n")
     bTree.postorder()
     print("\n\nInverse-In-Order Traversal:\n")
     bTree.inverse_inorder()
     
def menuTwoOptionTwo(bTree):
     print("\nAll Leaf nodes:\n")
     bTree.leaf_BST()
     print("\n\nAll Non-leaf nodes:\n")
     bTree.non_leaf_BST()
     
def menuTwoOptionThree(bTree):
     try:
         number = input("Enter a integer: ")
         number = int(number)
         bTree.total_nodesBST(number)
     except ValueError:
         print("Invalid input!!! Please enter a valid integer")
     

def menuTwoOptionFour(bTree):
    try:
         number = input("Enter a integer: ")
         number = int(number)
         bTree.depth_nodeBST(number)
    except ValueError:
         print("Invalid input!!! Please enter a valid integer")
    

def menuTwoOptionFive(bTree):
    try:
         number = input("Enter a integer: ")
         number = int(number)
         bTree.depth_subtreeBST(number)
    except ValueError:
         print("Invalid input!!! Please enter a valid integer")
     
    
def menuTwoOptionSix(bTree):
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

        
def menuTwoOptionSeven(bTree):
    try:
         number = input("Enter a integer: ")
         number = int(number)
         deleted = bTree.delete_(number)[0]
    except ValueError:
         print("Invalid input!!! Please enter a valid integer")
    if deleted == True:
        print("\nInteger", number, "has been deleted from BST")
        print("\n\nInverse-In-Order Traversal:\n")
        bTree.inverse_inorder()

#####################################################################
      
####################### Main Code ###################################
    
looping = True
while looping == True:    
    menuOneOption(optionInput(4,0,1))
