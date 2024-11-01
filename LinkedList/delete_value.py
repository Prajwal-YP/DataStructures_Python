from requests import delete


class Node:
    def __init__(self,value:int):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value:int):
        self.head=Node(value)
        self.tail=self.head

    def insert_end_tail(self,value:int):
        self.tail.next=Node(value)
        self.tail=self.tail.next

    def print_list(self):
        currentNode=self.head
        print('List values is as follows:')
        print('\t',end='')

        while(currentNode is not None):
            print(str(currentNode.value)+',', end='')
            currentNode=currentNode.next

        print('\b')

    def delete_value(self,value:int):
        currentNode=self.head

        if currentNode is None:
            return

        if currentNode.value==value:
            self.head=self.head.next

        while(currentNode.next is not None):
            if currentNode.next.value==value:
                currentNode.next=currentNode.next.next
                return
            currentNode=currentNode.next

# Creating the head node of the linked list
headNode=LinkedList(1)
headNode.insert_end_tail(10)
headNode.insert_end_tail(20)
headNode.insert_end_tail(30)
headNode.print_list()

value=int(input('Enter the value:\t'))
# Deleting the first element
headNode.delete_value(value)
headNode.print_list()

