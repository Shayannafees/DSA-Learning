class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
        

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='-->')
            current = current.next
        print('None') 

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next            #deleting head node case
            return

        prev = None
        while current and current.data != data: # type: ignore
            prev = current
            current = current.next

        if not current:
            print("Data not found in the list")
            return
        
        prev.next = current.next # type: ignore


    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


    def reverseLinkedList(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next # type: ignore
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    def isCycle(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next # type: ignore

            if slow == fast: 
                return True
        return False



    def findMid(self):
        slow, fast = self.head, self.head
        while fast and fast.next: # type: ignore
            slow = slow.next # type: ignore
            fast = fast.next.next # type: ignore
        
        return slow
    
    def getLength(self):
        counter = 0
        current = self.head
        while current:
            current = current.next
            counter += 1
        return counter
    
    def deleteAtPosition(self, position):
        if position < 0 or position >= self.getLength():
            print("Invalid position")
            return
        
        if position == 0:
            self.head = self.head.next # type: ignore
            return
        
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        counter = 1
        while current:
            if counter == position :
                current.next = current.next.next # type: ignore
                return
            current = current.next
            counter += 1
            

    def sort(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True        
                current = current.next
            



linked_list = SinglyLinkedList()

linked_list.insert(314)
linked_list.insert(78)
linked_list.insert(43)
linked_list.insert(640)
linked_list.insert(57)
linked_list.insert(69)
# print(linked_list.search(10))
# print(linked_list.getLength())
# linked_list.reverseLinkedList()
# linked_list.display()
# print('Cycle Detected?', linked_list.isCycle())
# linked_list.head.next.next.next = linked_list.head.next  # type: ignore
# print('Cycle Detected?', linked_list.isCycle())
# linked_list.deleteAtPosition(5)
# linked_list.display()
linked_list.display()
linked_list.sort()
linked_list.display()