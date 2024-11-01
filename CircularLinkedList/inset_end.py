class Node:
    def __init__(self,value:int):
        self.value=value
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.headNode:Node=None
        self.tailNode:Node=None

    def inset_beginning(self,value:int):

        new_node:Node=Node(value)
        
        if self.headNode is None:
            self.headNode=new_node
            self.headNode.next=self.headNode
            self.tailNode=self.headNode
            return 
        
        new_node.next=self.headNode
        self.headNode=new_node
        self.tailNode.next=new_node

    def insert_end(self,value):
        new_node=Node(value)

        if self.headNode is None:
            new_node.next=new_node
            self.headNode=new_node
            self.tailNode=new_node
            return

        new_node.next=self.headNode
        self.tailNode.next=new_node
        self.tailNode=new_node

    def print_values(self):
        current_node=self.headNode
        print('Values of circular linked list is :\t',end='')
        if current_node is None:
            return
        print(current_node.value,end=',')
        current_node=current_node.next
        while current_node!=self.headNode:
            print(current_node.value,end=',')
            current_node=current_node.next
        print('\b')


list1=CircularLinkedList()

list1.inset_beginning(400)
list1.inset_beginning(300)
list1.inset_beginning(200)
list1.inset_beginning(100)

list1.insert_end(500)
list1.print_values()
print('Tail node value:\t'+str(list1.tailNode.value))
