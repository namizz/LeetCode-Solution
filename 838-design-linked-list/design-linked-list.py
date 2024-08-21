class _Node:
    def __init__(self, value = None, next = None):
        self.next = next
        self.value = value
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        c = 0
        ll = self.head
        while ll and c< index:
            c += 1
            ll = ll.next
        return ll.value if ll else -1
        

    def addAtHead(self, val: int) -> None:
        node = _Node(val)
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        node = _Node(val)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        i = 0
        node = _Node(val)
        currentNode = self.head
        while i < index - 1 and currentNode:
            currentNode = currentNode.next
            i += 1
        if currentNode and currentNode.next:
            node.next = currentNode.next
            currentNode.next = node
        elif currentNode and i == index - 1:
            currentNode.next = node

        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if not current.next: 
                return
            current = current.next
        if current.next:
            current.next = current.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)