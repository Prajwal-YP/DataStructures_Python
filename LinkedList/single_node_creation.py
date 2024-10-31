class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

# Creating the head node of the linked list
headNode=Node(100)
print('Value of the head node is '+str(headNode.value))
