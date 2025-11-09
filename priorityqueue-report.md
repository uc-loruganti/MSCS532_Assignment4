# Priority Queue Simulation Report

## 1. Introduction

This report details the design, implementation, and analysis of a priority queue and its application in a simple task management simulation. The priority queue is implemented using a binary heap, and it is used to manage tasks with different priority levels.


## 2. Source Code

### 2.1. Task Class (`Task.py`)

The `Task` class is a simple data class that represents a task to be executed. It includes attributes such as `task_id`, `priority`, `arrival_time`, `deadline`, and a `description`.

The full source code can be found in the file [Task.py](Task.py).

### 2.2. Priority Queue Implementation (`priority-queue.py`)

The `PriorityQueue` is implemented as a min-priority queue using a binary heap. The heap is represented by a list.

The full source code for the `PriorityQueue` class can be found in the file [priority-queue.py](priority-queue.py).

### 2.3. Scheduler Simulation (`priority-queue.py` main block)

The main block in `priority-queue.py` provides a simple simulation of a task scheduler.

The scheduler simulation can be found in the `if __name__ == '__main__':` block in `priority-queue.py`.


## 3. Design Choices and Implementation Details

### 3.1. Priority Queue Design

A binary heap was chosen for the priority queue implementation. This data structure is well-suited for priority queues due to its efficiency in maintaining the heap property. Specifically, a min-heap is used, where the task with the lowest priority value is always at the root of the heap.

The heap is stored in a Python list, which provides a simple and effective way to represent the tree structure. The parent-child relationships are calculated using array indices.

```python
def _parent(self, i):
    return (i - 1) // 2

def _left_child(self, i):
    return 2 * i + 1

def _right_child(self, i):
    return 2 * i + 2
```

### 3.2. Implementation Details

- **`Task` Class:** A `dataclass` is used for the `Task` object for simplicity and clarity. It holds all the relevant information about a task.
- **`PriorityQueue` Class:**
    - The `heap` is a list of `Task` objects.
    - `_parent`, `_left_child`, and `_right_child` methods calculate the indices of related nodes in the heap.
    - `_swap` is a utility function to swap two elements in the heap.
    - `_shift_up` and `_shift_down` are used to maintain the heap property after insertion or deletion.
    - `insert` adds a new task and calls `_shift_up`.
    - `extract_min` removes the root element (minimum priority), replaces it with the last element, and calls `_shift_down` to restore the heap property.
    - `decrease_key` and `increase_key` find a task and update its priority, then call `_shift_up` or `_shift_down` respectively.

## 4. Analysis of Scheduling Results

The example usage in the `main` block of `priority-queue.py` simulates a basic scheduler.

1.  **Insertion:** Tasks are inserted into the priority queue. The heap structure ensures that the task with the lowest priority value is always at the front.
    ```python
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)
    ```
2.  **Extraction:** `extract_min` is used to get the highest-priority task (in this case, the one with the lowest priority number). This simulates a scheduler picking the next task to execute.
    ```python
    min_task = pq.extract_min()
    ```
3.  **Priority Changes:** `decrease_key` and `increase_key` simulate dynamic changes in task priorities. For example, a task's priority might be increased to ensure it meets a deadline.
    ```python
    pq.decrease_key(task1, 0)
    pq.increase_key(task3, 6)
    ```

The simulation demonstrates that the priority queue correctly manages the tasks, always providing the one with the highest priority upon request.

## 5. Time Complexity Analysis

The efficiency of the priority queue operations is crucial for a responsive scheduler.

- **`is_empty()`: O(1)**
  - Checks the length of the list, which is a constant time operation.
    ```python
    def is_empty(self):
        return len(self.heap) == 0
    ```

- **`insert(task)`: O(log n)**
  - Appending to the list is O(1). The `_shift_up` operation takes O(log n) time as it traverses the height of the heap.
    ```python
    def insert(self, task):
        self.heap.append(task)
        self._shift_up(len(self.heap) - 1)
    ```

- **`extract_min()`: O(log n)**
  - Swapping elements and popping from the end of the list are O(1). The `_shift_down` operation takes O(log n) time.
    ```python
    def extract_min(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        min_task = self.heap.pop()
        if not self.is_empty():
            self._shift_down(0)
        return min_task
    ```

- **`decrease_key(task, new_priority)`: O(n)**
  - Finding the task in the heap (`_find_task_index`) takes O(n) time as it may require scanning the entire list. The subsequent `_shift_up` is O(log n). The overall complexity is dominated by the search.
    ```python
    def decrease_key(self, task, new_priority):
        index = self._find_task_index(task)
        # ...
        self._shift_up(index)
    ```

- **`increase_key(task, new_priority)`: O(n)**
  - Similar to `decrease_key`, the search for the task is the bottleneck, resulting in O(n) complexity.
    ```python
    def increase_key(self, task, new_priority):
        index = self._find_task_index(task)
        # ...
        self._shift_down(index)
    ```

