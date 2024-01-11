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

# input: head and target
# output: head and remove target node from end
# create pointer left and right
# loop until right is pointing at target node
# loop until right is pointing at end and move left
# set left.next = left.next.next
# return head

def remove_nth_last_node(head, n):
    left = head
    right = head

    for i in range(n):
        right = right.next


    while right.next:
        left = left.next
        right = right.next

    left.next = left.next.next

    return head

lst1 = [23,28,10,5,67,39,70,28]
linked_list = LinkedList()
linked_list.create_linked_list(lst1)
head = linked_list.head

print(linked_list.__str__())
print(remove_nth_last_node(head, 2))
print(linked_list.__str__())
