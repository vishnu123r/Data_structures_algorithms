class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    def append (self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        
        if position == 1:
            return self.head

        if self.head:
            current = self.head
            counter = 1
            while current.next:
                current = current.next
                counter += 1
                if counter == position:
                    return current
            
            return None

    def insert(self, new_element, position):
        current = self.get_position(position)
        previous = self.get_position(position-1)
        if current:
            new_element.next = current
            previous.next = new_element
        else:
            self.append(new_element)

    def delete(self, value):
        current = self.head
        if value == current.value:
            self.head = current.next
            current.next == None
    
        while current.next:
            if current.next.value == value:
                deleted_value = current.next
                current.next == current.next.next
                deleted_value.next = None
                break

            current = current.next
                


if __name__ == "__main__":
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print (ll.head.next.next.value)
    # Should also print 3
    print (ll.get_position(3).value)

    # Test insert
    ll.insert(e4,3)
    # Should print 4 now
    print (ll.get_position(3).value)

    # Test delete
    ll.delete(1)

    # Should print 2 now
    print (ll.get_position(1).value)
    # Should print 4 now
    print (ll.get_position(2).value)
    # Should print 3 now
    print (ll.get_position(3).value)