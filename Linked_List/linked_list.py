class Node:
    def __init__(self , data):
        self.value = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def delete_node(self):
        if self.head is None:
            print("Can not delete")
        elif self.head.next is None:
            self.head = None 
        else:
            temp = self.head
            prev = temp
            while temp.next is not None :
                prev = temp
                temp = temp.next
            prev.next = None

    def print_ll(self):
        if self.head is  None:
            print("Linked list empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value ,end  = ' ')
                temp = temp.next
            print()  

    def find_length(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            temp = self.head
            count = 0
            while temp is not None:   
                count+=1
                temp = temp.next
            print("The length of the linked list is ",count)   

    def find_middle(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        print(slow_pointer.value)    

        
                     


l1 = LinkedList()
l1.add_node(30)
l1.add_node(40)
l1.add_node(50) 
l1.print_ll()
l1.find_middle()

