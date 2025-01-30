new_node.next = self.head
        self.head = new_node

        current = self.head
        while current.next != self.head: # type: ignore
            current = current.next # type: ignore
        