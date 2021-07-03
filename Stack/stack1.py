# Python program for implementation of stack

# Function to create a stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack
 
# Stack is empty when stack size is 0
def isEmpty(stack):
    return len(stack) == 0
 
# Function to add an item to stack. It increases size by 1
def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")
     
# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        print("Stack is empty")
    else: 
        print(stack.pop() + " popped from stack")
 
# Function to return the back from stack without removing it
def peek(stack):
    if (isEmpty(stack)):
        print("Stack is empty")
    else:
        print(stack[len(stack) - 1] + " is on the back of the stack")
 
# Driver program to test above functions   
stack = createStack()

push(stack, str(10))
print(stack)

push(stack, str(20))
print(stack)

push(stack, str(30))
print(stack)

pop(stack)
print(stack)

peek(stack)