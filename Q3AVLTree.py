#Student ID: 10636908
#Name: Poorav Sharma 

#############################################


outputdebug = True 

def debug(msg):
    if outputdebug:
        print (msg)

class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
#######################################                
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
                '''
    def getNode(self):
        return self.node
                '''
    
    def preorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist2 = []
        inlist2.append(self.node.key)
        inlist2 += self.node.left.preorder_traverse()

        inlist2 += self.node.right.preorder_traverse()
    
        return inlist2
    
    def postorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist3 = []        
        inlist3 += self.node.left.postorder_traverse()
        inlist3 += self.node.right.postorder_traverse()
        
        inlist3.append(self.node.key)
        return inlist3

    
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
    

     #one prints all leaf nodes
    def leaf_AVL(self):
        self.leaf_AVLHelper(self.node)
        
    def leaf_AVLHelper(self, r):
      if r != None:
        self.leaf_AVLHelper(r.left.node)       
        self.leaf_AVLHelper(r.right.node)
        if not r.left.node and not r.right.node:
            print(r.key, end = ", ")
            return

    #one prints all non_leaf nodes
    def non_leaf_AVL(self):
        self.non_leaf_AVLHelper(self.node)
        
    def non_leaf_AVLHelper(self, r):
      if r != None:
        self.non_leaf_AVLHelper(r.left.node)       
        self.non_leaf_AVLHelper(r.right.node)
        if r.left.node or r.right.node:
            print(r.key, end = ", ")
            return
        

    # Return True if the element is in the tree
    def search(self, e):
        node = self.node
    # Start from the root
        while node is not None:
            if e < node.key:
                node = node.left.node
            elif e > node.key:
                node = node.right.node
            else:  # element matches current.element
                return True, node  # Element is found

        return False, None 

        
    #Delete a node from the tree
    def delete_(self, key):
        if self.search(key):
            node = self.search(key)[1]
            self.delete_Helper(node, key)
            return True, self.node
        else:
            print("\nERROR: Node", key ," not found!")
            return False, key

    def delete_Helper(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left.node = self.delete_Helper(node.left.node, key)
        elif key > node.key:
            node.right.node = self.delete_Helper(node.right.node, key)
        else:
            if node.left.node is None and node.right.node is None:
                return None
            if node.left.node is None:
                return node.right.node
            if node.right.node is None:
                return node.left.node
            successor = self.logical_successor(node)
            node.key = successor.key
            node.right.node = self.delete_Helper(node.right.node, successor.key)

        self.rebalance()
        return node
    
    def findSuc(self, node):
        while self.node.left is not None:
            node = self.node.left
        return node
    
    def printTree(self):                                
        def display(root):                                     
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            #   No child.
            if root.node.right.node is None and root.node.left.node is None:
                line = str(root.node.key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            #   Only left child.
            if root.node.right.node is None:
                lines, n, p, x = display(root.node.left)
                nodeOutput = (str(root.node.key) )
                keyLength = len(nodeOutput)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput
                second_line = x * ' ' + '/' + (n - x - 1 + keyLength) * ' '
                shifted_lines = [line + keyLength * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, n + keyLength // 2

            #   Only right child.
            if root.node.left.node is None:
                lines, n, p, x = display(root.node.right)
                nodeOutput = str(root.node.key)
                keyLength = len(nodeOutput)
                first_line = nodeOutput + x * '_' + (n - x) * ' '
                second_line = (keyLength + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [keyLength * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, keyLength // 2

            #   Two children.
            left, n, p, x = display(root.node.left)
            right, m, q, y = display(root.node.right)
            nodeOutput = str(root.node.key)
            keyLength = len(nodeOutput)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + keyLength + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + keyLength * ' ' + b for a, b in zipped_lines]
            return lines, n + m + keyLength, max(p, q) + 2, n + keyLength // 2

        lines = []
        if self.node != None:
            lines, *_ = display(self)
            print("\t\t=== AVL Tree ===")
            print()
        if lines == []:
            print("No tree found, please rebuild a new Tree.\n")
            return -1
        for line in lines:
            print(line)
        print()
        
class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None
        
#############################################
#method displays the options that the user can pick from    
def optionDisplay(displayNumber):     
    if displayNumber == 1:
        print("\n\nQuestion 3: AVL tree: deleting a node\n")
        print("\n1. Pre-load a sequence of integers to build a AVL tree \n")
        print("2. Manually enter integer values/keys, one by one, to build an AVL tree\n")
        print("3. Exit\n")
    elif displayNumber == 2:
        print("\n\n\nQuestion 3: AVL tree: deleting a node\n")
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
    aTree = AVLTree()    
    inputtoTree(aTree, sequence)
    
    while True:
        optionNumber = optionInput(7, 0, 2)
        if optionNumber == 1:
            menuTwoOptionOne(aTree)
        elif optionNumber == 2:
            menuTwoOptionTwo(aTree)
        elif optionNumber == 3:
            menuTwoOptionThree(aTree)
        elif optionNumber == 4:
            menuTwoOptionFour(aTree)
        elif optionNumber == 5:
            menuTwoOptionFive(aTree)          
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

def menuTwoOptionOne(aTree):
    aTree.printTree()
    print("\n == AVL tree (printed left-side down, with [hights, balance_factors] & an \'L\' for each leaf node) ==\n")
    aTree.display()
     
     
     
def menuTwoOptionTwo(aTree):
    print("\nPre-Order Traversal:\n")
    print(aTree.preorder_traverse())
    print("\n\nIn-Order Traversal:\n")
    print(aTree.inorder_traverse())
    print("\n\nPost-Order Traversal:\n")
    print(aTree.postorder_traverse())
     
def menuTwoOptionThree(aTree):
    print("\nAll Leaf nodes:\n")
    aTree.leaf_AVL()
    print("\n\nAll Non-leaf nodes:\n")
    aTree.non_leaf_AVL()
     

def menuTwoOptionFour(aTree):
    try:
         number = input("Enter a integer: ")
         number = int(number)
         inserted = aTree.insert(number)
    except ValueError:
         print("Invalid input!!! Please enter a valid integer")
    if inserted ==True:
        print("\nInteger", number, "has been inserted into the AVL")
    

def menuTwoOptionFive(aTree):
    try:
         number = input("Enter a integer: ")
         number = int(number)
         deleted = aTree.delete_(number)[0]
    except ValueError:
         print("Invalid input!!! Please enter a valid integer")
    if deleted == True:
        print("\nInteger", number, "has been deleted into the AVL")
        
     
    

#####################################################################
      
####################### Main Code ###################################
    
looping = True
while looping == True:    
    menuOneOption(optionInput(4,0,1))
