class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def change_val(self,val):
        self.val = val

    def change_next(self, next):
        self.next = next

class linkedList:
    def __init__(self):
        self.head = Node()

    def append(self, val):
        newNode = Node(val)
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.val)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' index out of range")
            return None

        cur = self.head
        for i in range(index+1):
            cur = cur.next
        
        return cur.val

    def erase(self,index): 
        if index >= self.length():
            print("Error 'erase' index out of range")
            return None

        pre = self.head
        cur = self.head.next
        for i in range(index):
            pre = pre.next
            cur = cur.next

        pre.next = cur.next
        return


        
        

myList = linkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.display()
myList.erase(2)
myList.display()


