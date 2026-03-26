class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError("Source list cannot be empty")
    
    node_to_move = source
    new_source = source.next
    node_to_move.next = dest
    
    return Context(new_source, node_to_move)