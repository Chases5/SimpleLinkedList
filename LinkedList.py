class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self,val):
            self.nextNode = None
            self.val = val

    def insert(self, val):
        if self.head is None:
            self.head = self.Node(val) #
            return
        current = self.head
        while current.nextNode is not None:
            current = current.nextNode
        current.nextNode = self.Node(val)

    def remove(self, val):
        if self.head is None:
            return False
        if self.head.val == val:
            self.head = self.head.nextNode
            return True
        current = self.head
        while current.nextNode is not None:
            if current.nextNode.val == val:
                current.nextNode = current.nextNode.nextNode
                return True
        return False

    def printVal(self):
        current = self.head
        string = ""
        while current is not None:
            string += (str(current.val) + ", ")
            current = current.nextNode
        print(string)

if __name__ == "__main__":
    print("tests")
    list = LinkedList()
    print("test insertions")
    list.insert("t")
    list.printVal()
    list.insert(1)
    list.printVal()
    list.insert(2)
    list.printVal()
    print("test deletion")
    list.remove(1)
    list.printVal()
    list.remove("t")
    list.printVal()
