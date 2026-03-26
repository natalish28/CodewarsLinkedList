def stringify(node):
    if node is None:
        return 'None'
    new_list = []
    current = node
    while current is not None:
        new_list.append(current.data)
        current = current.next
        
    new_list.append("None")
    return " -> ".join(str(i) for i in new_list)
