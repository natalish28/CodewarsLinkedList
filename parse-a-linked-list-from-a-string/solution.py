from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None
    parts = list_repr.split(' -> ')
    part = parts.pop()
    current = None
    for i in reversed(parts):
        current = Node(int(i), current)

    return current 