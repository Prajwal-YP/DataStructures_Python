class Node:
    def __init__(self,value:int):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value:int):
        self.head=Node(value)
        self.tail=self.head

    def insert_at_kth_position(self,kthPosition:int,value:int):
        newNode=Node(value)
        currentNode=self.head
        currentPosition=1

        if kthPosition==1:
            self.insert_beginning(value)

        while(currentPosition<kthPosition-1):
            if currentNode.next is None:
                print('insertion not possible at this position-'+str(kthPosition))
                return
            currentNode=currentNode.next
            currentPosition+=1


        newNode.next=currentNode.next
        currentNode.next=newNode


    def insert_beginning(self,value:int):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode

    def insert_end_tail(self,value:int):
        self.tail.next=Node(value)
        self.tail=self.tail.next

    def insert_end_loop(self,value:int):
        newNode=Node(value)
        currentNode=self.head

        if currentNode is None:
            self.head=newNode
            return
        
        while(currentNode.next is not None):
            currentNode=currentNode.
            
        currentNode.next=newNode
        self.tail=newNode

    def print_list(self):
        currentNode=self.head
        print('List values is as follows:')
        print('\t',end='')
        
        while(currentNode is not None):
            print(str(currentNode.value)+',', end='')
            currentNode=currentNode.next
        
        print('\b')


# Creating the head node of the linked list
headNode=LinkedList(1)
headNode.insert_end_loop(2)
headNode.insert_end_loop(3)
headNode.insert_end_loop(4)
headNode.print_list()

headNode.insert_at_kth_position(5,22)
headNode.print_list()
