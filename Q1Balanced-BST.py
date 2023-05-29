#Student ID: 10636908
#Name: Poorav Sharma 

#The method below is very useful to display the binary tree so that he user can understand the shap if the tree more easily. The comments below is the source of the code and the person who uploaded it online. 
##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
##  AUTHOR: Original: J.V.     Edit: BcK
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
    print("\t== Balanced Binary Tree: ==")
    print()
    if lines == []:
        print("\t  No tree found")
    for line in lines:
        print("\t", line)
    print()


#method displays the options that the user can pick from    
def optionDisplay(displayNumber):     
    if displayNumber == 1:
        print("\nQuestion 1 Balanced BST generation \n")
        print("\n1. Pre-load a sequence of integers to build a balanced BST \n")
        print("2. Manually enter integer values, one by one, to build a balanced BST\n")
        print("3. Exit\n")
 
        
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

#this method deals with the option that the users has chosen    
def chosenOption(optionNumber):
    if optionNumber == 1:
        optionOne()
    elif optionNumber == 2:
        optionTwo()
    else:
        print("\nExiting\n")
        exit()
#first option us the pre loaded sequence. it will be sorted and displayed as a balanced binary tree
def optionOne():
    #the sequence below was required to be tested
     preSequence = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]

    #use this sequence below if you want to test another sequence
     #preSequence = [-2, 17, 94, -55, 36, -9, 12, -83, 68, 7, -76, 45, -30, 59, 0, -42, 81, -98, 23]
     print("Pre-Loaded sequence: \n")
     print(preSequence, "\n")
 
     print("Pre-Loaded sequence reorganized: \n") 
     inputSequence = createNewSequence(preSequence)
     
     print(inputSequence, "\n")
     treeNodes = inputtoTree(inputSequence)
     printTree(treeNodes)
         
     
#second option will ask for u to add integer into the sequence. the sequence will be sorted and displayed as a balanced binary tree
def optionTwo():
     userSequence = inputInteger()
     print("User sequence: \n")
     print(userSequence, "\n")

     print("User sequence reorganized: \n") 
     inputSequence = createNewSequence(userSequence)
     print(inputSequence, "\n")
     treeNodes = inputtoTree(inputSequence)
     printTree(treeNodes)
     
     
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
            
#sort the sequence in an ascending order
def sortSequence(sequence):
    elementNumber = len(sequence) 
    for i in range(elementNumber):
        minimumIndex = i;
        for j in range(i+1, elementNumber):
            if sequence[j]<sequence[minimumIndex]:
                minimumIndex = j
        swap(sequence, i, minimumIndex)
    return sequence
        
#method to swap the elements if the current element is bigger or smaller than the next element in the array
def swap (array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

def inputtoTree(sequence):
    bTree = BinaryTree()
    for element in sequence:
        bTree.insert(element)
    return bTree.getRoot()

#these following classes for creating binary tree were made thanks to the Module 6 in canvas  
class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None


#create the binary tree class
class BinaryTree:
    #create the node of the tree    
    def __init__(self):
        self.root = None
        self.size = 0 
        
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
              return False # Duplicate node not inserted

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

#sort the sequence and find the middle elemet to make the root node.
#it then moves on to reverse the all the elements from the beginning to the middle so that it is in desending order so that the tree can be created that way
#the right side of the middle sequence stays the same because it is already in acending order. 
def createNewSequence(sequence):
    if not sequence:
        return []
    
    sortedSequence = sequence[:]
    sortedSequence = sortSequence(sortedSequence)
    inputSequence =[]   
    
    mid = (len(sortedSequence)) // 2
    
    inputSequence.append(sortedSequence[mid])
    leftSequence = sortedSequence[:mid]    
    rightSequence = sortedSequence[mid+1:]    
    
    inputSequence.extend(createNewSequence(leftSequence))
    inputSequence.extend(createNewSequence(rightSequence))
    
    return inputSequence

##################################################################    

######################### Main Code ##############################


looping = True
while looping == True:    
    chosenOption(optionInput(4,0,1))



      

