class Node:
    def __init__(self, data, next= None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtEnd(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head: # type: ignore
                current = current.next # type: ignore
            current.next = new_node # type: ignore  
            new_node.next = self.head

    def insertAtBeginning(self,data):
        new_node = Node(data)

        current = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while current.next != self.head: # type: ignore
                current = current.next # type: ignore
            current.next = new_node # type: ignore
        self.head = new_node 

    def searchElem(self, data):
        if not self.head:
            print('List is empty')
            return False
        if self.head.data == data:                              #head node's data equals data, will return true
            return True

        current = self.head.next                                 #starting from 2nd node as 1st has been checked
        while current != self.head: # type: ignore              
            if current.data == data: # type: ignore
                return True
            current = current.next # type: ignore
        return False


    def deleteNodebyValue(self,data):
        if not self.head:
            print("List is empty")
            return
        
        if self.head.data == data:                                              #if 1st node is required deleted node
            if self.head.next == self.head:                                         #if there is only one node
                self.head = None
                return 
            
            # self.head = self.head.next                                          #2nd node will become head node
            last = self.head
            while last.next != self.head: # type: ignore
                last = last.next # type: ignore
            self.head = self.head.next
            last.next = self.head # type: ignore
            return


        current = self.head # type: ignore
        while current.next != self.head: # type: ignore                         #avoiding list to become circular
            if current.next.data == data: # type: ignore
                current.next = current.next.next # type: ignore
                return
            current = current.next # type: ignore
            
    def countNodes(self):
        if not self.head:
            return 0
        counter = 1
        current = self.head
        while current.next != self.head: # type: ignore
            counter += 1
            current = current.next # type: ignore
        return counter
    
    def reverseCll(self):
        if not self.head:                                       #if no node at all
            print("Empty list can't be reversed")
            return
        current = self.head
        if current.next == self.head:                       #if only 1 node, reverse will be the same node
            return self.head
        
        prev = None
        while True: # type: ignore
            next_node = current.next # type: ignore
            current.next = prev # type: ignore
            prev = current
            current = next_node

            if current == self.head:
                break
        
        self.head.next = prev
        self.head = prev

    def splitInTwoHalves(self):
        if not self.head:
            print("List can't be split")
            return None, None
        
        if self.head.next == self.head:
            print("Only one node, can't split")
            return self.head, None

        slow, fast = self.head, self.head

        while fast.next != self.head and fast.next.next != self.head: # type: ignore
            slow = slow.next # type: ignore
            fast = fast.next.next # type: ignore

        first_half = self.head
        second_half = slow.next # type: ignore
        slow.next = first_half # type: ignore

        temp = second_half
        while temp.next != self.head: # type: ignore
            temp = temp.next # type: ignore
        temp.next = second_half # type: ignore

        return first_half, second_half
    

    def display(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while current:
            print(current.data, end='-->') # type: ignore
            current = current.next # type: ignore
            if current == self.head:
                break
        print('Loops back to head')

s = LinkedList()

s.insertAtBeginning(20)
s.insertAtBeginning(10)
s.insertAtEnd(30)
s.insertAtEnd(40)

print("Original Circular Linked List:")
s.display()

# Splitting the circular linked list
first_half, second_half = s.splitInTwoHalves()

# Displaying the two halves
if first_half:
    print("\nFirst Half:")
    first_list = LinkedList()
    first_list.head = first_half
    first_list.display()

if second_half:
    print("\nSecond Half:")
    second_list = LinkedList()
    second_list.head = second_half
    second_list.display()

# print(s.searchElem(50))
# s.deleteNodebyValue(40)
# print(s.countNodes())
# s.reverseCll()
# s.display()

    # def insertAtBeginning(self, data):
    #     new_node = Node(data)
        
    #     if not self.head:
    #         self.head = new_node # type: ignore
    #         self.head.next = self.head #or new_node         # type: ignore            #making it circular, if there's only 1 node.
    
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node

    #         current = self.head
    #         while current.next != self.head: # type: ignore
    #             current = current.next # type: ignore
    #         current.next = new_node # type: ignore

    


