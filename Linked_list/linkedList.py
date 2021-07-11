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
print("Inserting a few numbers: {}\n".format(numbers))

# removing from the head
numbers.remove_head()
print("After removing head: {}\n".format(numbers))

# using the iterator to print all the numbers in LinkedList
print("All numbers in LinkedList:")
for x in numbers:
    print(x)