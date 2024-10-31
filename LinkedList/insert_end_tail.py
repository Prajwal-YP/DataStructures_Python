class Node:
    def __init__(self,value:int):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value:int):
        self.head=Node(value)
        self.tail=self.head

    def insert_beginning(self,value:int):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode

    def insert_end_tail(self,value:int):
        self.tail.next=Node(value)
        self.tail=self.tail.next


# Creating the head node of the linked list
headNode=LinkedList(1)
print('Value of the tail node is '+str(headNode.tail.value))

headNode.insert_end_tail(2)
print('Value of the tail node is '+str(headNode.tail.value))

headNode.insert_end_tail(3)
print('Value of the tail node is '+str(headNode.tail.value))

headNode.insert_end_tail(4)
print('Value of the tail node is '+str(headNode.tail.value))
