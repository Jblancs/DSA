from utils import LinkedList, reverse_linked_list, traverse_linked_list

# input: head of singly LL
# output: middle node

# initialize fast and slow pointer
# while fast and fast.next
# increment slow by 1 and fast by 2
# return slow

# time: O(n)
# space: O(1)


def get_middle_node(head):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

list_1 = LinkedList()
list_1.create_linked_list([1,2,3,4,5,6])
print(get_middle_node(list_1.head).data)
