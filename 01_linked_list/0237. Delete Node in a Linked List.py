"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Since we do not have access to the node before the one we want to delete, we cannot modify the next pointer of that node in any way. Instead, we have to replace the value of the node we want to delete with the value in the node after it, and then delete the node after it.
"""

def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
