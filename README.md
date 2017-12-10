[![Build Status](https://travis-ci.org/han8909227/data-structures.svg?branch=master)](https://travis-ci.org/han8909227/data-structures)
# Data Structure
Various data structure written in python by Han Bao and Phillip Werner


# Linked-Lists

Linked list, where each node has a one way reference to the next.

- Push: O(1)
    - Insert given value to the head

- Pop: O(1)
    - Remove the head value

- Size: O(1)
    - Returns the current size

- Search: O(n)
    - Searches for the given value

- Remove: O(n)
    - Remove the given value

- Display: O(n)
    - Display the current list as a string of tuple

- \__len\__: O(1)
    - Declare len() method which returns the value from self.size()


# Doubly-Linked-Lists

Doubly-Linked-Lists, where each node has two way reference to its previous and next node.

- Push: O(1)
    - Insert given value to the head

- Pop: O(1)
    - Remove the head value

- Append: O(1)
    - Insert given value to the tail

- Shift: O(1)
    - Remove the tail value

- Remove: O(n)
    - Remove the given value from the list

- \__len\__: O(1)
    - Declare len() method which returns the value from self.size()


# Stack

FILO (First In Last Out), where the frist node pushed in is the last node that will be pop.

- Push: O(1)
    - Insert given value to the head

- Pop: O(1)
    - Remove the head value

- \__len\__: O(1)
    - Declare len() method which returns the value from self.size()


# Queues

FIFO (First In First Out), where the first node enqueued is the first node that will be dequeued.

- Enqueue: O(1)
    - Insert given value to the tail

- Dequeue: O(1)
    - Remove the head value

- \__len\__: O(1)
    - Declare len() method which returns the value from self.size()


# Deque

Ordered list, where each node has two way reference to its previous and next node.

- Append: O(1)
    - Insert given value to the tail

- Append_Left : 0(1)
    - Insert given value to the head

- Pop: O(1)
    - Remove the tail value

- Pop_Left: 0(1)
    - Remove the head value

- Peek: O(1)
    - Returns the tail value

- Peek_Left: O(1)
    - Returns the head value

- Size: 0(1)
    - Returns the size of the deque

- \__len\__: O(1)
    - Declare len() method which returns the value from self._counter.


# Binheap

Min heap that stores value using min-heap artictiure

- Push: O(N)
    - Insert a value into the heap, perculate up to proper node.

- Pop: O(N)
    - Pop the top value from the heap(min value for min heap)


# Graph (weighted & directional)

A graph structure where each node can be direct/point to another node.

- nodes: O(n)
    - return a list of all nodes in the graph.

- edges: O(n^2)
    - return a list of all edges in the graph.

- add_node: O(1)
    - add a new node to the graph if not already existed.

- add_edge: O(1)
    - add a new directed edge from the two nodes inputted, add node(s) if not existed.

- del_node: O(n)
    - delete the given node from the graph, raise error if no such node exists.

- del_edge: O(1)
    - delete the edge from inputted nodes(1 to 2), raise error if no such edge exists.

- has_node: O(1)
    - return true if given node is in the graph, false if it's not.

- neighbors: O(1)
    - return a list of all nodes the given node can reach(directed to).

- adjacent: O(1):
    - return true if an edge exist between node 1 and node 2 (either direction), false otherwise.

- breath_first_traversal: O(n)
    - return values from the starting node using BFT

- depth_first_traversal: O(log(n))
    - return values from the starting node using DFT

# Priority Queues
An queue where data is sorted by the priority level which it was passed in with, the one with highest priority and earliest entered is removed first. (FIFO with priority)

- Insert: O(1)
    - Insert the value into the priority queue with the priority level passed in.

- Pop: O(n log(n))
    - Pop off a value from the highest priority bin, the one that entered that bin firsted.

- Peek: O(n log(n))
    - Peek at the value that is about to be popped.


# Binary search tree(non self-balancing)
A binary tree search non self balacing data structure

- Insert: O(log(n)
    - Insert the value into the binary search tree.

- Search: O(log(n))
    - Search for a node containing the value being search.

- Size: O(1)
    - Return the current size of the tree.

- Depth: O(n)
    - Return the current depth (deepst) of the tree structure. (0 for no root or root only tree)

- Contains: O(n)
    - Return boolean value for wehther the value exists in the tree.

- Balance: O(n)
    - Return the current balance state of the tree, negative if tree is higher on the left and positive otherwise. Balanced tree will have a value of zero.

- In Order Traversal: O(n)
    - Return a generator object that goes through values in the tree via in order traversal

- Post Order Traversal: O(n)
    - Return a generator object that goes through values in the tree via post order traversal

- Pre Order Traversal: O(n)
    - Return a generator object that goes through values in the tree via pre order traversal

- Delete: O(log(n))
    - Delete the node with value being passed in


# Hash table
A Hash table that acts like python dictionary, insert keys via hashed locations.

- Set: O(1)
    - Insert a key, value pair into the current hash table

- Get: O(n)
    - Extract the value corresponding to the key given


# Trie
A prefix tree that allows insertion and deletion of worfds

- Insert: O(1)
    - Insert a word or string into the prefix tree

- Contains: O(n)
    - Return True if word/str passed in is in the tree, False otherwise

- Remove: O(n)
    - Remove an existing word/str from the tree

- Size: O(1)
    - Look up the current size(num of words) in the tree

- Traversal: O(n)
    - Return a generator object generate through words in the trie one at a time


# Bubble Sort O(n^2)
A sorting algorithm taking a list or tuple of numbers and sort
them according to respective numerical values.


# Insertion Sort O(n^2)
A sorting algorithm taking a list or tuple of numbers and sort
them according to respective numerical values.