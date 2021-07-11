'''
Solution to the try it yourself challenge
'''

class LinkedList:
    class Node:

        # Initialize the node. Links are unknown so set to None
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    # Initialize an empty linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert a new node at the head of the liked list
    def insert_head(self, value):
        new_node = LinkedList.Node(value)

        # If the linked list is empty, make new_node the linked list
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # else add new_node to the head of existing linked list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    # Insert into the middle of the linked list after a given value
    def insert_middle(self, value, new_value):
        new_node = LinkedList.Node(value)
        curr = self.head

        # If the location of value is at the tail, we make this the new tail
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                # For all other instances, we will make a new node and update the pointers
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            curr = curr.next

    # Insert to the tail
    def insert_tail(self, value):
        new_node = LinkedList.Node(value)

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


    # Remove head from linked list
    def remove_head(self):
        # If there is only one node, set pointers to None
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # if more than one, remove head
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next

    # Remove from the middle of linked list at a value
    def remove_middle(self, value):
        curr = self.head

        while curr is not None:
            if curr.data == value:
                curr.next.prev = curr.prev
                curr.prev.next = curr.next
            curr = curr.next

    # Remove the tail from linked list
    def remove_tail(self):
        if self.tail == self.head:
            self.head = None
            self.tail = None

        elif self.head is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
    
    # iterator
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next
    
    # This function returns a string representation of the linked list
    # for use in the test cases
    def __str__(self):
        output = "linkedlist["
        first = True
        curr = self.head
        while curr is not None:
            if first:
                first = False
            else:
                output += ", "
            output += str(curr.data)
            curr = curr.next
        output += "]"
        return output

# testing our linked list

# create an empty linked list
numbers = LinkedList()
print("Empty linked list: {}\n".format(numbers))

# insert some numbers at the head of our linked list
numbers.insert_head(1)
numbers.insert_head(2)
numbers.insert_head(3)
numbers.insert_head(4)
numbers.insert_head(5)
print("Inserting a few numbers: {}\n".format(numbers))
# [5, 4, 3, 2, 1]

# removing from the head
numbers.remove_head()
print("After removing head: {}\n".format(numbers))
# [4, 3, 2, 1]

# insert 8 after 2
numbers.insert_middle(2, 8)
print("After inserting to midddle: {}\n".format(numbers))
# [4, 3, 2, 8, 1]

# insert 10 at the tail
numbers.insert_tail(10)
print("After inserting at tail: {}\n".format(numbers))
# [4, 3, 2, 8, 1, 10]

# Remove the tail
numbers.remove_tail()
print("After removing the tail: {}\n".format(numbers))
# [4, 3, 2, 8, 1]

# Remove 2 from the middle of the linked list
numbers.remove_middle(2)
print("After removing 2 from LinkedList: {}\n".format(numbers))
# [4, 3, 8, 1]

# using the iterator to print all the numbers in LinkedList
print("All numbers in LinkedList:")
for x in numbers:
    print(x)
# 4 3 8 1