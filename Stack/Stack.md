# Stack

## Overview
* [What is a stack?](#what-is-a-stack)
* [Using a stack](#using-a-stack)
    * Stack of plates
    * Undo Function
* [Operations](#operations)
    * Push
    * Pop
    * Size
    * Empty
* [Performance](#performance)
* [Code Example](#code-example)
* [Try it Yourself!](#try-it-yourself)


## What is a Stack?
A stack is a data structure that follows a particular order in which the operations are to be performed. The order is primarily refered to as *"Last in, First Out"* or *"LIFO"*. The stack can be used to complete many different tasks, and in this tutorial will be implemented with a python list.

## Using a Stack
### **A Stack of Plates**
To explain how a stack works, we will be using the example of a stack of plates at a buffet line. When you want to add a plate to the stack, you are only able to add to the top of the stack. If you want to take away a plate, you can only remove from the top.

![Stack animation](Stack.gif)

A stack in Python works much the same way. Adding to the back of the stack is called a **Push**. Removing from the back of the stack is called a **Pop**. Normally you do not **push** or **pop** from the middle of the stack as that is not as efficient as working from the back. We will talk more about performance later.

### **Undo Function**
Another example of how a stack can be used is in an undo function seen in most word processing programs. The words you type are **pushed** onto the stack. This creates a history of what has been typed. When you press undo the words are **poped** off of the stack. Lets look at an example.

![Undo Example](Undo.jpg)

On the first stack shown, we can see the phrase *"The quick brown fox jumps over the lazy dog"*. Each word was **Pushed** onto the stack one by one until the entire phrase was stored. 

On the second stack, we can see that when the undo button is pressed, it will **Pop** from the back of the stack. We can see on the second stack that the word *"Dog"* has been removed. If we undo four more times, four more items will be **Popped** off of the stack as shown in the third stack.

Now we can add five more words to the stack. If we type *"scurries under the red barn"*, we can see that each word was **Pushed** onto the stack replacing the original phrase.

## Operations
Lets review some of the operations of a stack.

| Stack Operations | Description | Python Code | Performance |
|-|-|-|-|
| push(value)|Adds "value" the the back of the stack.|stack.append(value)|O(1) Performance of adding to the end of a dynamic array|

## Performance

## Code Example

## Try it Yourself!

Ready of the [next challenge](../Linked_list/Linked_list.md)? or [Return to overview](../README.md)
