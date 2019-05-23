class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def traversal(self, head):
        current_node = head # starting from the head node
        while current_node is not None:
            print(current_node.val)
            current_node = current_node.next
    
    def insertion(self, head, value):
        current_node = head
        while current_node is not None:
            if current_node.next is None:
                current_node.next = Node(value)
                return head
            current_node = current_node.next

    def delete(head, value):
        current_node = head
        previous_node = None
        while current_node is not None:
            if current_node.val == value:
                if previous_node is None: # if the value to remove is the head node
                    new_head = current_node.next
                    current_node.next = None # detach the node from the linked list
                    return new_head
                previous_node.next = current_node.next
                return head
            previous_node = current_node
            current_node = current_node.next
        return head # value to delete was not found
