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

    def insert_end_loop(self,value:int):
        newNode=Node(value)
        currentNode=self.head

        if currentNode is None:
            self.head=newNode
            return

        while(currentNode.next is not None):
            currentNode=currentNode.next

        currentNode.next=newNode
        self.tail=newNode

# Creating the head node of the linked list
headNode=LinkedList(1)
print('Value of the head node is '+str(headNode.tail.value))

headNode.insert_end_loop(2)
print('Value of the head node is '+str(headNode.tail.value))

headNode.insert_end_loop(3)
print('Value of the head node is '+str(headNode.tail.value))

headNode.insert_end_loop(4)
print('Value of the head node is '+str(headNode.tail.value))
