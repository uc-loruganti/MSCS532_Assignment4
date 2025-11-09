# MSCS532_Assignment4

## Reports
Heap sort analysis : [HeapSort-Analysis.md](HeapSort-Analysis.md)

Priority Queue analysis: [priorityqueue-report.md](priorityqueue-report.md)


## Heap Sort

The `heap-sort.py` script implements the Heap Sort algorithm. You can run it from the command line:

### Usage
```bash
python heap-sort.py --elements <comma-separated-integers>
```

### Example
```bash
python .\heap-sort.py --elements 12, 12, 13, 5, 6, 7
Heap Sort Implementation
Original array: [12, 12, 13, 5, 6, 7]
Sorted array: [5, 6, 7, 12, 12, 13]
```

## Priority Queue

The `priority-queue.py` script implements a Priority Queue using a min-heap. The `Task.py` script defines a `Task` class that is used in the priority queue. You can run the priority queue script from the command line:

```bash
python priority-queue.py
```

The script will perform a series of operations on the priority queue and print the state of the queue after each operation.
```
Priority Queue after inserting tasks:
Task ID: 2, Priority: 1
Task ID: 1, Priority: 3
Task ID: 3, Priority: 2
Task ID: 4, Priority: 5
Task ID: 5, Priority: 4

Extracted task with min priority: Task ID: 2, Priority: 1

Priority Queue after extracting min task:
Task ID: 3, Priority: 2
Task ID: 1, Priority: 3
Task ID: 5, Priority: 4
Task ID: 4, Priority: 5

Decreasing priority of Task ID: 1 to 0

Priority Queue after decreasing key:
Task ID: 1, Priority: 0
Task ID: 3, Priority: 2
Task ID: 5, Priority: 4
Task ID: 4, Priority: 5

Increasing priority of Task ID: 3 to 6

Priority Queue after increasing key:
Task ID: 1, Priority: 0
Task ID: 4, Priority: 5
Task ID: 5, Priority: 4
Task ID: 3, Priority: 6

Extracting all tasks:
Task ID: 1, Priority: 0
Task ID: 5, Priority: 4
Task ID: 4, Priority: 5
Task ID: 3, Priority: 6
```