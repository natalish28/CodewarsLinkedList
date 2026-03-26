from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node is None or index < 0:
        raise Exception("Invalid index or empty list")
    count = 0
    current = node

    while current is not None:
        if count == index:
            return current
        
        current = current.next
        count += 1
    raise Exception("Index out of bounds")
