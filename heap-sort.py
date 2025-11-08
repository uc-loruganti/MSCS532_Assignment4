import argparse

# To heapify a subtree rooted with node index which is an index in arr[]. length is size of heap
def heapify(arr, length, index):
    largest = index 
    # Find the largest among root, left child and right child
    left = 2 * index + 1
    right = 2 * index + 2

    # print(f"largest={largest}, index={index}, length={length}, arr={arr}")

    # See if left child of root exists and is greater than root
    if left < length and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < length and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        # Swap and continue heapifying if root is not largest
        arr[index], arr[largest] = arr[largest], arr[index]
        # Recursively heapify the affected sub-tree
        heapify(arr, length, largest)

# Main function to do heap sort
def heap_sort(arr):
    length = len(arr)

    # print(length)
    height = (length // 2) - 1

    # Build max heap
    for i in range(height, -1, -1):
        # heapify the current node
        heapify(arr, length, i)
        
    # One by one extract elements from heap
    for i in range(length - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # call max heapify on the reduced heap
        heapify(arr, i, 0) 
    return arr

if __name__ == "__main__":
    print("Heap Sort Implementation")
    parser = argparse.ArgumentParser(description="Heap Sort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    input_array = args.elements
    # input_array = [12, 11, 13, 5, 6, 7]
    print("Original array:", input_array)
    sorted_array = heap_sort(input_array)
    print("Sorted array:", sorted_array)
    