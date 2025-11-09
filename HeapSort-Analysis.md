# Heap Sort Analysis

## Time Complexity

Heapsort has a time complexity of **O(n log n)** in the worst, average, and best cases. This is implemented in the `heap_sort` function in [heap-sort.py](heap-sort.py).

### Worst-case, Average-case, and Best-case: O(n log n)

The Heapsort algorithm consists of two main phases:

1.  **Building the heap:** This phase takes an unsorted array and arranges it into a max-heap. In `heap-sort.py`, this is done in the first `for` loop of the `heap_sort` function.
    
    ```python
    # Build max heap
    for i in range(height, -1, -1):
        # heapify the current node
        heapify(arr, length, i)
    ```
    
    This loop calls the `heapify` function for each non-leaf node. For an array of size `n`, there are `n/2` non-leaf nodes. The `heapify` function takes O(log n) time. A naive analysis would suggest that building the heap takes O(n log n) time. However, a tighter analysis shows that this `build_max_heap` process takes **O(n)** time. This is because the height of the heap is `log n`, and while the root can take `log n` swaps, the nodes at the bottom take very few swaps.

2.  **Sorting:** This phase repeatedly extracts the maximum element from the heap (which is always the root) and places it at the end of the array. In `heap-sort.py`, this is done in the second `for` loop of the `heap_sort` function.
    
    ```python
    # One by one extract elements from heap
    for i in range(length - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # call max heapify on the reduced heap
        heapify(arr, i, 0)
    ```
    
    After each extraction, the heap is restored by calling `heapify` on the root of the smaller heap. This is done `n-1` times. Each `heapify` operation takes O(log n) time. Therefore, this phase takes **O(n log n)** time.

The overall time complexity of Heapsort is dominated by the sorting phase, which is **O(n log n)**. Since the `heapify` operation's performance is not dependent on the initial order of the elements, the best, worst, and average-case time complexities are all the same.

## Space Complexity

Heapsort is an **in-place** sorting algorithm, meaning it requires a constant amount of extra space. The space complexity is **O(1)**. The sorting is done within the original array `arr`. A few variables are needed to store indices and temporary values during swaps, but this does not scale with the input size `n`.

## Additional Overheads

*   **Not Stable:** Heapsort is not a stable sort. The relative order of equal elements may not be preserved.
*   **Cache Performance:** Heapsort can have poor cache performance because it jumps around in memory when accessing heap elements. This can make it slower in practice than algorithms like Quicksort, especially for large datasets. The `heapify` function accesses elements at `index`, `2 * index + 1`, and `2 * index + 2`, which can be far apart in memory.

## Empirical Comparison with Quicksort and Merge Sort

While Heapsort, Quicksort, and Merge Sort all have an average time complexity of O(n log n), their practical performance varies due to factors like memory access patterns, stability, and space complexity.

### Input Distributions

*   **Random Data:** For random data, **Quicksort** is often the fastest in practice. Its inner loop is simple and has good cache performance. Heapsort tends to be slower than Quicksort due to its less cache-friendly memory access patterns (jumping between parent and child nodes). Merge Sort is also very efficient but may be slightly slower than Quicksort due to the overhead of the merge step.

*   **Sorted or Nearly Sorted Data:** In this case, a naive implementation of **Quicksort** can degrade to its worst-case O(n^2) performance if the pivot is always chosen as the first or last element. However, with a good pivot selection strategy (e.g., median-of-three), Quicksort can still perform well. **Heapsort's** performance is not affected by the initial order of the data, so it remains O(n log n). **Merge Sort** also remains O(n log n) and is a good choice for nearly sorted data.

*   **Reverse-Sorted Data:** Similar to sorted data, **Quicksort** can degrade to O(n^2) with a poor pivot strategy. **Heapsort** and **Merge Sort** are unaffected and maintain their O(n log n) performance.

### Observed Results vs. Theoretical Analysis

| Algorithm   | Best Case     | Average Case    | Worst Case    | Space Complexity | Stable | In-place |
|-------------|---------------|-----------------|---------------|------------------|--------|----------|
| **Heapsort**  | O(n log n)    | O(n log n)      | O(n log n)    | O(1)             | No     | Yes      |
| **Quicksort** | O(n log n)    | O(n log n)      | O(n^2)        | O(log n)         | No     | Yes      |
| **Merge Sort**| O(n log n)    | O(n log n)      | O(n log n)    | O(n)             | Yes    | No       |

*   **Heapsort's** main advantage is its **O(1) space complexity** and guaranteed **O(n log n) time complexity**. However, in practice, it is often slower than Quicksort due to poor cache locality. The memory accesses in Heapsort are scattered throughout the array, leading to more cache misses.

*   **Quicksort** is often the fastest in practice for average cases due to its **excellent cache performance** and low constant factors in its implementation. Its main drawback is the potential for a **worst-case O(n^2) running time**, although this is rare with good pivot selection.

*   **Merge Sort's** strength is its **guaranteed O(n log n) performance** and **stability**. However, it requires **O(n) extra space**, which can be a significant drawback for large datasets.

In summary, while Heapsort has an excellent theoretical profile in terms of time and space complexity, its real-world performance can be impacted by hardware characteristics like cache memory. Quicksort is often preferred for its speed in the average case, while Merge Sort is chosen when stability or guaranteed worst-case performance is crucial and extra space is not a concern.
