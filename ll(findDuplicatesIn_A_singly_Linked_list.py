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


    def findDuplicates(self):
        current = self.head
        set1 = set()
        prev = None
        first_pass = True
        while first_pass or current != self.head:
            first_pass = False
            if current.data in set1: # type: ignore
                prev.next = current.next # type: ignore
                print(f"Duplicate {current.data} is removed") # type: ignore
            else:
                set1.add(current.data) # type: ignore
                prev = current
            current = current.next # type: ignore
        return set1

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
            print('Loops back to end')

s = LinkedList()
s.insertAtBeginning(20)
s.insertAtBeginning(10)
s.insertAtBeginning(10)
s.insertAtEnd(30)
s.insertAtEnd(30)
s.insertAtEnd(40)
s.findDuplicates()
s.display()