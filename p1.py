class Node:
    def __init__(self):
        self.leftLink = None
        self.data = int(input('Enter data of the new Node: '))
        self.rightLink = None

class BST:
    def __init__(self):
        self.root = None

    def insertNode(self):
        newNode = Node()
        if self.root == None:
            self.root = newNode
            return        
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if newNode.data < temp1.data:
                temp1 = temp1.leftLink
            else:
                temp1 = temp1.rightLink
        if newNode.data < temp2.data:
            temp2.leftLink = newNode
        else:
            temp2.rightLink = newNode

    def insertNodeRecursively(self, temp):
        if temp == None:
            newNode = Node()
            return newNode
        if newNode.data < temp.data:
            temp.leftLink = self.insertNodeRecursively(temp.leftLink)
        else:
            temp.rightLing = self.insertNodeRecursively(temp.rightLink)
        return temp

    def inOrder(self, temp):
        if temp != None:
            self.inOrder(temp.leftLink)
            print(temp.data)
            self.inOrder(temp.rightLink)

    def preOrder(self, temp):
        if temp != None:
            print(temp.data)
            self.preOrder(temp.leftLink)
            self.preOrder(temp.rightLink)

    def postOrder(self, temp):
        if temp != None:
            self.postOrder(temp.leftLink)
            self.postOrder(temp.rightLink)
            print(temp.data)

    def deleteNode(self):
        pass

class Menu:
    def __init__(self, treeObject):
        self.treeObject = treeObject

    def exitProgram(self):
        exit('End of Program')
    
    def invalidChoice(self):
        print('Invalid choice entered')

    def getDataManupalationMenu(self):
        menu = {
            1 : self.treeObject.insertNode,
            2 : self.treeObject.deleteNode,
            6 : self.exitProgram
        }
        return menu
    
    def getTreeTraversalMenu(self):
        menu = {
            3 : self.treeObject.inOrder,
            4 : self.treeObject.preOrder,
            5 : self.treeObject.postOrder
        }
        return menu

    def runMenu(self):
        menu1 = self.getDataManupalationMenu()
        menu2 = self.getTreeTraversalMenu()
        while True:
            choice = int(input('1:Insert 2:Delete 3:InOrder 4:PreOrder 5:PostOrder 6:Exit  Your choice Plz: '))
            if choice >= 3 and choice <= 5:
                menu2.get(choice, self.invalidChoice)(self.treeObject.root)
            else:
                menu1.get(choice, self.invalidChoice)()

def startApp():
    treeObject = BST()
    menuObj = Menu(treeObject)
    menuObj.runMenu()

startApp()

'''
insert at position:
If invalid position is given (bigger than length of the list) then new node is inserted at rare. 
delete specific node
if invalid positon is given, then error msg is printed
display list
'''