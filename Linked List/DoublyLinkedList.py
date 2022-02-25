class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return

        node = Node(data,self.head,None)
        self.head.prev = node
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None,itr)
    
    def insert_at(self, index, data):
        if self.head is None or index < 0 or index > self.get_length():
            raise Exception("Invalid Index!\n")
        
        if index == 0:
            self.insert_at_begining(data)
            return

        if index == self.get_length():
            self.insert_at_end(data)
            return
        
        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                node = Node(data,itr.next,itr)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count+=1

    def insert_values(self, data_list):

        for val in data_list:
            self.insert_at_end(val)
        

        

    def print_forward(self):

        if self.head is None:
            print("Linked List is empty.\n")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr = llstr + str(itr.data) + "-->"
            itr = itr.next
        print(llstr,"\n")

    def print_backward(self):
        if self.head is None:
            print("Doubly Linked List is empty.\n")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr = str(itr.data) + "-->" + llstr
            itr = itr.next
        print(llstr,"\n")

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr.data

        
    def get_length(self):
        count = 0
        
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def remove_at(self, index):
        if self.head is None:
            raise Exception("Invalid Index!\n")
        
        if index == 0:
            
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0

        while itr:

            if count == index:

                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

        


if __name__ == '__main__':
    dll = DoublyLinkedList()

    dll.insert_at_begining(2)
    dll.insert_at_begining(1)

    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(6)

    dll.insert_at(0,0)
    dll.insert_at(5,5)

    dll.insert_at(7,7)
    dll.insert_at(0,-1)
    
    count = dll.get_length()
    dll.insert_at(count,10)

    values = ["banana", "mango", "orange"]
    dll.insert_values(values)
    
    dll.print_forward()
    dll.print_backward()
    count = dll.get_length()
    print(f"Doubly Linked List length: {count}\n")

    lastNode = dll.get_last_node()
    print("Last Node is: ", lastNode,"\n")



