class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    '''
    Space: O(1)
    Time: O(n)
    '''

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= 0 and index < self.size:
            curr = self.head
            for i in range(index):
                curr = curr.next
            return curr.val
        else:
            return -1

    '''
    Space: O(1)
    Time: O(1)
    '''

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        head = Node(val)
        head.next = self.head
        self.head = head
        self.size += 1

    '''
    Space: O(1)
    Time: O(n)
    '''

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tail = Node(val)
        curr = self.head
        for i in range(self.size - 1):
            curr = curr.next
        curr.next = tail
        self.size += 1

    '''
    Space: O(1)
    Time: O(n)
    '''

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index < self.size:
            curr = self.head
            node = Node(val)
            for i in range(index - 1):
                curr = curr.next
            prev = curr
            curr = curr.next
            node.next = curr
            prev.next = node
            self.size += 1

    '''
    Space: O(1)
    Time: O(n)
    '''

    def deleteAtIndex(self, index: int) -> None:
      """
        Delete the index-th node in the linked list, if the index is valid.
        """
       if index == 0 and self.size > 0:
            self.head = self.head.next
            self.size -= 1
        elif index > 0 and index < self.size:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            prev = curr
            curr = curr.next
            nxt = None if curr is None else curr.next
            prev.next = nxt
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
