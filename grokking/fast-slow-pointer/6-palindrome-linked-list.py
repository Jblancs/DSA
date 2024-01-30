# input: head of LL
# output: boolean if palindrome

# init fast and slow pointers
# while loop curr and curr.next
# reassign slow to slow.next
# reassign fast to fast.next.next
# call reverse_linked_list(slow)
# compare lists using loop
# return False if list1.val != list2.val
# return True

from utils import LinkedList, reverse_linked_list

def palindrome(head):

    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    rev_list = reverse_linked_list(slow)
    rev_curr = rev_list
    curr = head
    while rev_curr is not None:
        if curr.data != rev_curr.data:
            return False
        curr = curr.next
        rev_curr = rev_curr.next

    return True

list_1 = LinkedList()
list_1.create_linked_list([1,2,3,2,1])
print(palindrome(list_1.head))
list_2 = LinkedList()
list_2.create_linked_list([4,7,9,5,4])
print(palindrome(list_2.head))
list_3 = LinkedList()
list_3.create_linked_list([2,3,5,5,3,2])
print(palindrome(list_3.head))
