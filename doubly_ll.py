class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def insertAtBeginning(self, data):
        new_node = Node(data)


        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    
    def insertAtEnd(self, data):
        new_node = Node(data)

        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def displayHeadToTail(self):
        current = self.head
        while current:
            print(current.data, end='<-->' if current.next else '-->')
            current = current.next
        print('None')


    def displayTailToHead(self):
        current = self.tail
        while current:
            print(current.data, end='<-->' if current.prev else '-->')
            current = current.prev
        print('None')

    def deleteFromBeginning(self):
        if not self.head:
            print("List is empty!")
            return
        
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        
        self.head = self.head.next # type: ignore
        self.head.prev = None # type: ignore

    def deleteFromEnd(self):
        if not self.head:
            print("List is empty!")
            return
        if self.head == self.tail:
            self.head, self.tail = None, None
        
        self.tail = self.tail.prev # type: ignore
        self.tail.next = None # type: ignore

    def insertAtPosition(self, data, position):
        new_node = Node(data)
        if not self.head or position == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        current = self.head
        counter = 0
        while current and counter < position - 1:       # traversing until it reaches one elem before where we will insert new_node.
            current = current.next                      
            counter += 1                                    
        
        next_node = current.next # type: ignore         # tracking node that will come after new node

        new_node.prev = current                         # fitting new node in between and making current node previous to new node
        new_node.next = next_node                       # making next_node(saved/tracked earlier), new_node's next node
        current.next = new_node # type: ignore          # again ensuring next node of current is new_node
        if next_node:
            next_node.prev = new_node # type: ignore      # net_node previous node is new_node
        else:
            self.tail = new_node                        # if there was no node next to current node prior to inserting new_node, tail is now new_node.

    def deleteAtPosition(self,postion):
        if not self.head:
            print("List is already empty")

        if postion == 0:                                #if deleting head node
            if self.head == self.tail:                  #if there's only one node
                self.head, self.tail = None, None       #making list empty
            else:
                self.head = self.head.next # type: ignore
                self.head.prev = None # type: ignore
            return      

        current = self.head
        counter = 0
        while current and counter < postion:                #traversing until the position, which has to be removed
            current = current.next
            counter += 1

        if not current:
            print("Position out of bounds!!")
            return
        


        if current == self.tail: # type: ignore            #checking if node is last node which has to be deleted, we will make 2nd last node tail.
            self.tail = self.tail.prev # type: ignore
            self.tail.next = None # type: ignore
            return
        
        #general case, deleting in the middle
        current.prev.next = current.next # type: ignore
        if current.next:
            current.next.prev = current.prev


    def reverseList(self):
        current = self.head
        temp = None

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp

            current = current.prev

        if temp:
            self.head = temp.prev

            


s = DoublyLinkedList()
s.insertAtBeginning(30)
s.insertAtBeginning(20)
s.insertAtBeginning(10)
# s.insertAtPosition(15,1)
# s.insertAtPosition(25,3)
# s.insertAtPosition(5,0)

s.displayHeadToTail()                       #printing before operations
# s.deleteAtPosition(1)                       #deleting at position 1
# s.displayHeadToTail()                       #printing after deletion
s.reverseList()
s.displayHeadToTail()

# s.deleteAtPosition(5)                       #deleting at postion 5
# s.deleteAtPosition(0)                       #deleting head node
# s.deleteAtPosition(3)                       #deleting tail
# s.deleteFromEnd()
# s.deleteFromBeginning()
# s.displayTailToHead()