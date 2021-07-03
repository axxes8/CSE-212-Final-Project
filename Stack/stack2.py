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
    # print(item + " pushed to stack ")
     
# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        print("Stack is empty")
    else: 
        stack.pop()
 
# Function to return the back from stack without removing it
def peek(stack):
    if (isEmpty(stack)):
        print("Stack is empty")
    else:
        print(stack[len(stack) - 1])

def stringToStack(string):
    for letter in string:
        push(stack, letter)
    result = ""
    while len(stack) > 0:
        result += stack.pop()
    return result
 
# Driver program to test above functions   
stack = createStack()

print(stringToStack("racecar"))
#racecar

print(stringToStack("stressed"))
#desserts

print(stringToStack("a nut for a jar of tuna"))
#anut fo raj a rof tun a