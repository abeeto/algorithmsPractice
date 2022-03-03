# Priority Queues Notes

## what are priority queues?
priority queue is an ADT, similar to queue
but each item has an additional attribute - a value to denote its priority/position in line
selforganizing based on priorities - highest priority is removed first


## how can they be implemented?
queues are implemented by a list. 
priority queues are normally implemented using a heap.
a heap is a tree based data structure that satisifies the heap property/invariant
heap property/invariant: if A is a parent node of B then A is ordered with respect to B for all nodes A, B in the heap.

So if A is a parent of a node of B either A is greater or less than B

heaps are probably best represented using arrays

## when and where is a pq used?
- used in djikstra's shortest path algorithm, to fetch the next node to explore
- anytime you need to dynamically fetch the next best or next worst element
- huffman coding
- best first search
- minimum spanning tree algorithms (prims)

## how to turn a min pq into a max pq
maybe use post or pre order traversal and recursively swap the nodes until you get a new heap (bubble down)

## time complexity
| Operation                |Complexity|
| ------------------------ | -------  |
| Binary Heap Construction | O(n)     |
| Polling                  | O(logn)  |
| Peeking                  | O(1)     |
| Adding                   | O(logn)  |

There are ways to reduce complexities for some operations by using a hash table. 


## binary heap pq implementation


## heap sinking and swimming (aka bubble up and down)


## adding elements to pq


## removing elements to pq
