# input: head of linked list
# output: boolean whether linked list contains cycle

# initialize fast and slow pointer to head
# while fast != null
# if fast.data == slow.data return True
# if fast.data == null return False
# slow = slow.next
# fast = fast.next.next

# time = O(logn)
# space = O(1)

def detect_cycle(head):
    if head is None:
        return False

    slow, fast = head, head

    while fast != None and fast.next:

        slow = slow.next
        fast = fast.next.next

        if fast == slow:
           return True

    return False



class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # returns the number of nodes in the linked list
    def get_length(self, head):
        temp = head
        length = 0
        while(temp):
            length+=1
            temp = temp.next
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


list_1 = LinkedList()
list_1.create_linked_list([2,4,6,8,10])

list_2 = LinkedList()
list_2.create_linked_list([1,3,5,7,9])

print(detect_cycle(list_1.head))
print(detect_cycle(list_2.head))
