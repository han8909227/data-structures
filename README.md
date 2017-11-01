# Data Structure
Various data structure written in python by Han Bao and Phillip Werner



# Linked-Lists

Ordered list, where each node has a one way reference to the next.

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

Ordered list, where each node has two way reference to its previous and next node.

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
