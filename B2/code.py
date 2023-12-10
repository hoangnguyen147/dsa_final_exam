class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def append_linked_list(head, data):
    new_node = Node(data)

    if head is None:
        head = new_node
    else:
        current_node = head
        while(current_node.next is not None):
            current_node = current_node.next

        current_node.next = new_node

def remove_duplicates(head):
    if head is None:
        return None
    current_node = head
    visited = set()
    visited.add(current_node.data)

    while current_node.next is not None:
        if current_node.next.data in visited:
            current_node.next = current_node.next.next
        else:
            visited.add(current_node.next.data)
            current_node = current_node.next

    return head

def display(head):
    current_node = head
    while current_node.next is not None:
        print(current_node.data, end=" -> ")
        current_node = current_node.next


head = Node(1)
append_linked_list(head, 2)
append_linked_list(head, 2)
append_linked_list(head, 3)
append_linked_list(head, 2)
append_linked_list(head, 3)
append_linked_list(head, 4)
append_linked_list(head, 4)
append_linked_list(head, 5)
append_linked_list(head, 6)


display(remove_duplicates(head))