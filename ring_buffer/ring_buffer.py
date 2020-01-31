from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        """Adds elements to the buffer."""
        # If the length of the buffer is less than its capacity...
        if self.storage.length < self.capacity:
            # Add the item to the tail.
            self.storage.add_to_tail(item)
            # This is the oldest item.
            self.current = self.storage.head

        # If the buffer is at capacity...
        else:
            # The item to be deleted.
            del_item = self.storage.head
            # Remove the oldest item.
            self.storage.remove_from_head()
            # Add the item to the tail.
            self.storage.add_to_tail(item)
            
            # If the item to be deleted is the same as the current item...
            if del_item == self.current:
                # Becomes the oldest item.
                self.current = self.storage.tail

    def get(self):
        """Returns all of the elements in the 
        buffer in a list in their given order."""
        # Note: This is the only [] allowed.
        list_buffer_contents = []
        
        first_node = self.current
        list_buffer_contents.append(first_node.value)

        # If there are nodes after the first node...
        if first_node.next is not None:
            next_node = first_node.next

        else:
            next_node = self.storage.head

        # As long as the next node doesn't equal the first node...
        while next_node != first_node:
            list_buffer_contents.append(next_node.value)

            if next_node.next is not None:
                next_node = next_node.next

            else:
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
