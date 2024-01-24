from utils import LinkedList

# input: head of linked list
# output: boolean whether linked list contains cycle

# initialize fast and slow pointer to head
# while fast != null
# if fast.data == slow.data return True
# if fast.data == null return False
# slow = slow.next
# fast = fast.next.next

# time = O(n)
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


list_1 = LinkedList()
list_1.create_linked_list([2,4,6,8,10])

list_2 = LinkedList()
list_2.create_linked_list([1,3,5,7,9])

print(detect_cycle(list_1.head))
print(detect_cycle(list_2.head))
