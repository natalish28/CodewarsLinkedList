class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("list is too short")
    
    first = None
    second = None
    current = head
    
    while current is not None and current.next is not None:
        first = push(first, current.data)
        second = push(second, current.next.data)
        current = current.next.next
    
    if current is not None:
        first = push(first, current.data)
    
    first = reverse(first)
    second = reverse(second)
    
    return Context(first, second)