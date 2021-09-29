class node:
    def __init__(self,val=None):
        self.val = val
        self.l = None
        self.r = None

    
class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root == None:
            self.root = node(val)
        else:
            self._insert(val,self.root)

    def _insert(self, val, cur):
        if val < cur.val:
            if cur.l == None:
                cur.l = node(val)
            else:
                self._insert(val,cur.l)
        elif val > cur.val:
            if cur.r == None:
                cur.r = node(val)
            else:
                self._insert(val,cur.r)
        else:
            print("value already in tree: ", val)

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self,cur):
        if cur != None:
             self._printTree(cur.l) 
             print(str(cur.val))
             self._printTree(cur.r)

    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        return 0

    def _height(self,cur,cur_height):
        if cur == None: return cur_height
        leftHeight = self._height(cur.l, cur_height+1)
        rightHeight = self._height(cur.r, cur_height+1)
        return max(leftHeight,rightHeight)

    def search(self,val):
        if self.root!=None:
            return self._search(val,self.root)
        return False

    def _search(self,val,cur):
        if cur == None:
            return False
        elif val == cur.val:
            return True
        elif val < cur.val:
            return self._search(val,cur.l)
        elif val > cur.val:
            return self._search(val,cur.r)

        

tree = binaryTree()

tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(0)
tree.insert(6)
tree.insert(7)
tree.insert(8)

tree.printTree()
print(tree.search(5))
print(tree.search(10))