from preloaded import Node

def swap_pairs(head):
    dummy = Node(next=head)
    prev = dummy
    
    while prev.next is not None and prev.next.next is not None:
        A = prev.next
        B = prev.next.next
        
        prev.next = B
        A.next = B.next
        B.next = A
        
        prev = A
    
    return dummy.next