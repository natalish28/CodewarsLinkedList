""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head is None:
        return Node(data)

    if data < head.data:
        return push(head, data)

    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    
    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node

    return head

