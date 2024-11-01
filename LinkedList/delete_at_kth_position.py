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

    def delete_beginning(self):
        if self.head is None:
            print('list is empty')
            return

        self.head=self.head.next

    def delete_at_kth_position(self,kthPosition:int):
        if (kthPosition<1):
            print('Invalid position')
            return
        if(kthPosition==1):
            self.delete_beginning()
            return

        currentNode=self.head
        currentPosition=1

        if currentNode is None:
            print('list is empty')
            return

        while(currentPosition<kthPosition-1):
            currentNode=currentNode.next
            if currentNode.next is None:
                print('invalid position')
                return
            currentPosition+=1

        currentNode.next=currentNode.next.next

# Creating the head node of the linked list
headNode=LinkedList(1)
headNode.insert_end_tail(10)
headNode.insert_end_tail(20)
headNode.insert_end_tail(30)
headNode.print_list()

kthPosition=int(input('Enter the position at which you want to delete the element:\t'))
# Deleting the first element
headNode.delete_at_kth_position(kthPosition)
headNode.print_list()

