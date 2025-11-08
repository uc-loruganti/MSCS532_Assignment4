# Heap Sort Implementation in Python
def heapify(arr, length, index):
    largest = index 
    left = 2 * index + 1
    right = 2 * index + 2

    print(f"largest={largest}, index={index}, length={length}, arr={arr}")

    if left < length and arr[left] > arr[largest]:
        largest = left

    if right < length and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, length, largest)

def heap_sort(arr):
    length = len(arr)

    print(length)
    height = (length // 2) - 1
    
    # Build max heap
    for i in range(height, -1, -1):
        heapify(arr, length, i)
        
    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0) 
    return arr

if __name__ == "__main__":
    print("Heap Sort Implementation")
    input_array = [12, 11, 13, 5, 6, 7]
    print("Original array:", input_array)
    sorted_array = heap_sort(input_array)
    print("Sorted array:", sorted_array)
    