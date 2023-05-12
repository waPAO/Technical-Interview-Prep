'''
Given two sorted linked lists, merge them so that the resulting linked 
list is also sorted.

assume the linkedlists are not empty
'''

'''
pseudocode

create a node class
make a linkedlist class
create merge function
set trackers for both heads
traverse through lists and heck if head is greater than the other
append to the new linkedlist
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
      
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

def merge(a, b):
    sorted_ll = LinkedList()
    head_a = a.head
    head_b = b.head

    while head_a and head_b:
        if head_a.val < head_b.val:
            sorted_ll.insert(head_a.val)
            head_a = head_a.next
        else:
            sorted_ll.insert(head_b.val)
            heab_b = heab_b.next
    return sorted_ll