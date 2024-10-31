class Node:
    def __init__(self,value:int):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value:int):
        self.head=Node(value)

    def insert_beginning(self,value:int):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode

    def get_head_value(self):
        if self is None:
            return None
        else:
            return self.head.value

# Creating the head node of the linked list
headNode=LinkedList(3)
print('Value of the head node is '+str(headNode.head.value))

# Inserting element at the beginning of the linked list
headNode.insert_beginning(2)
print('Value of the head node is '+str(headNode.head.value))

headNode.insert_beginning(1)
print('Value of the head node is '+str(headNode.head.value))

headNode.insert_beginning(4)
print('Value of the head node is '+str(headNode.head.value))
