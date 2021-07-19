class BST:
    class Node:
        # initialize our node. Currently the links are unknown, so they are set to None.
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):
        # initialize an empty BST
        self.root = None

    def insert(self, data):
        # If our BST is empty make our new node the root
        if self.root is None: 
            self.root = BST.Node(data)
        # if not empty call our recursive function
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        # If data is less than our node...
        if data < node.data:
            # If left node is empty insert data
            if node.left is None:
                node.left = BST.Node(data)
            # Else, call _insert() again and start on the left node
            else:
                self._insert(data, node.left)
        # If data is greater than our node...
        else:
            # If right node is empty insert data
            if node.right is None:
                node.right = BST.Node(data)
            # Else, call _insert() again and start on the right node
            else:
                self._insert(data, node.right)

    def __iter__(self):
        # Start at the root of the tree
        yield from self._traverse_reverse(self.root)
    
    def _traverse_reverse(self, node):
        # If the node is not empty traverse the tree
        if node is not None:
            yield from self._traverse_reverse(node.right)
            yield node.data
            yield from self._traverse_reverse(node.left)

# Test cases
tree = BST()
tree.insert(63)
tree.insert(32)
tree.insert(18)
tree.insert(85)
tree.insert(25)
tree.insert(36)


for x in tree:
    print(x)