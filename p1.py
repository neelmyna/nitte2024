class Node:
    def __init__(self):
        self.data = input('Enter data of the new Node: ')
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self):
        position = int(input('Enter position of the new node: '))
        node = Node()
        if self.head == None:
            self.head = node
            return
        if position == 1:
            node.link = self.head
            self.head = node
            return
        temp = self.head
        i = 2
        while temp.link != None and i < position:
            i += 1
            temp = temp.link
        if temp.link == None:
            temp.link = node
            return
        node.link = temp.link
        temp.link = node

    def displayList(self):
        if self.head == None:
            print('List is empty')
            return
        temp = self.head
        while temp != None:
            if temp.link != None:
                print(temp.data + ' -> ', end='')   
            else:
                print(temp.data)
            temp = temp.link

    def deleteNode(self):
        if self.head == None:
            print('List is empty')
            return
        position = int(input('Enter the position of the node to be deleted: '))
        if position == 1:
            print(f'Node with data {self.head.data} is deleted')
            self.head = self.head.link
            return
        i = 1
        temp2 = None
        temp1 = self.head
        while temp1.link != None and i < position:
            i += 1
            temp2 = temp1
            temp1 = temp1.link
        if temp1.link == None and position > i:
            print('Invalid position enetered')
            return
        if i == position-1 and temp1.link == None:
            print(f'Node with data {temp1.data} is deleted')
            temp2.link = None
            return
        print(f'Node with data {temp1.data} is deleted')
        temp2.link = temp1.link

class Menu:
    def __init__(self, listObject):
        self.listObject = listObject

    def exitProgram(self):
        exit('End of Program')
    
    def invalidChoice(self):
        print('Invalid choice entered')

    def getMenu(self):
        menu = {
            1 : self.listObject.insertNode,
            2 : self.listObject.deleteNode,
            3 : self.listObject.displayList,
            4 : self.exitProgram
        }
        return menu
    
    def runMenu(self):
        menu = self.getMenu()
        while True:
            choice = int(input('1:Insert 2:Delete 3:DisplayList 4:Exit Your choice Plz: '))
            menu.get(choice, self.invalidChoice)()

def startApp():
    list = LinkedList()
    menuObj = Menu(list)
    menuObj.runMenu()

startApp()

'''
insert at position:
If invalid position is given (bigger than length of the list) then new node is inserted at rare. 
delete specific node
if invalid positon is given, then error msg is printed
display list
'''