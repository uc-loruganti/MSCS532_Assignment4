from Task import Task

class PriorityQueue:
    """
    Implements a min-priority queue using a binary heap structure.
    The heap is internally represented using a list for efficient memory usage.
    """
    def __init__(self):
        self.heap = []

    def is_empty(self):
        """
        Checks if the priority queue is empty.
        Time complexity: O(1)
        """
        return len(self.heap) == 0

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _shift_up(self, i):
        """
        Moves an element up the heap to maintain the heap property.
        """
        while i > 0 and self.heap[self._parent(i)].priority > self.heap[i].priority:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def insert(self, task):
        """
        Add a task to the heap-based priority queue.
        Time complexity: O(log n) with respect to the number of tasks.
        """
        self.heap.append(task)
        self._shift_up(len(self.heap) - 1)

    def _shift_down(self, index):
        """
        Moves an element down the heap to maintain the heap property.
        """
        min_index = index
        left = self._left_child(index)
        if left < len(self.heap) and self.heap[left].priority < self.heap[min_index].priority:
            min_index = left
        right = self._right_child(index)
        if right < len(self.heap) and self.heap[right].priority < self.heap[min_index].priority:
            min_index = right
        if index != min_index:
            self._swap(index, min_index)
            self._shift_down(min_index)

    def extract_min(self):
        """
        Removes and returns the task with the smallest priority.
        Time complexity: O(log n), where n is the number of tasks in the queue.
        """
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        min_task = self.heap.pop()
        if not self.is_empty():
            self._shift_down(0)
        return min_task

    def _find_task_index(self, task):
        """
        Finds the index of a given task in the heap.
        Time complexity: O(n)
        """
        for i, t in enumerate(self.heap):
            if t.task_id == task.task_id:
                return i
        return -1

    def decrease_key(self, task, new_priority):
        """
        Lowers a task's priority and shifts it upward to restore the heap property.
        Time complexity: O(n) due to the linear search for the task.
        """
        index = self._find_task_index(task)
        if index == -1:
            return False
        
        if new_priority >= self.heap[index].priority:
            return False # New priority is not smaller

        self.heap[index].priority = new_priority
        self._shift_up(index)
        return True

    def increase_key(self, task, new_priority):
        """
        Increase a task's priority and shift it downward to restore the heap property.
        Time complexity: O(n) due to the linear search for the task.
        """
        index = self._find_task_index(task)
        if index == -1:
            return False

        if new_priority <= self.heap[index].priority:
            return False # New priority is not larger

        self.heap[index].priority = new_priority
        self._shift_down(index)
        return True

if __name__ == '__main__':
    # Example Usage
    # 1. Create a Priority Queue
    pq = PriorityQueue()

    # 2. Create some tasks
    task1 = Task(task_id=1, priority=3, arrival_time=0, deadline=10)
    task2 = Task(task_id=2, priority=1, arrival_time=1, deadline=5)
    task3 = Task(task_id=3, priority=2, arrival_time=2, deadline=8)
    task4 = Task(task_id=4, priority=5, arrival_time=3, deadline=12)
    task5 = Task(task_id=5, priority=4, arrival_time=4, deadline=15)

    # 3. Insert tasks into the priority queue
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)
    pq.insert(task4)
    pq.insert(task5)

    print("Priority Queue after inserting tasks:")
    for task in pq.heap:
        print(f"Task ID: {task.task_id}, Priority: {task.priority}")

    # 4. Extract the task with the minimum priority
    min_task = pq.extract_min()
    print(f"\nExtracted task with min priority: Task ID: {min_task.task_id}, Priority: {min_task.priority}")

    print("\nPriority Queue after extracting min task:")
    for task in pq.heap:
        print(f"Task ID: {task.task_id}, Priority: {task.priority}")

    # 5. Decrease the priority of a task
    print(f"\nDecreasing priority of Task ID: {task1.task_id} to 0")
    pq.decrease_key(task1, 0)

    print("\nPriority Queue after decreasing key:")
    for task in pq.heap:
        print(f"Task ID: {task.task_id}, Priority: {task.priority}")

    # 6. Increase the priority of a task
    print(f"\nIncreasing priority of Task ID: {task3.task_id} to 6")
    pq.increase_key(task3, 6)

    print("\nPriority Queue after increasing key:")
    for task in pq.heap:
        print(f"Task ID: {task.task_id}, Priority: {task.priority}")

    # 7. Extract all tasks
    print("\nExtracting all tasks:")
    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Task ID: {task.task_id}, Priority: {task.priority}")
