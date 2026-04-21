import random
import time

# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Merge sort
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# Quick sort
def partition(arr, low, high):

    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Timing function
def measure_time(sort_func, arr):
    arr_copy = arr.copy()

    start = time.time()

    if sort_func == quick_sort:
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        result = sort_func(arr_copy)
        if result is not None:
            arr_copy = result

    end = time.time()
    return (end - start) * 1000  # ms


# Dataset generator
def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = {}

    random.seed(42)  

    for size in sizes:
        random_list = [random.randint(1, 100000) for _ in range(size)]
        sorted_list = list(range(size))
        reverse_list = list(range(size, 0, -1))

        datasets[(size, "Random")] = random_list
        datasets[(size, "Sorted")] = sorted_list
        datasets[(size, "Reverse")] = reverse_list

    return datasets


# Correctness check
def check_correctness():
    test = [5, 2, 9, 1, 5, 6]
    print("Original:", test)

    arr1 = test.copy()
    insertion_sort(arr1)
    print("Insertion:", arr1)

    arr2 = merge_sort(test.copy())
    print("Merge:", arr2)

    arr3 = test.copy()
    quick_sort(arr3, 0, len(arr3) - 1)
    print("Quick:", arr3)

    print("Expected: [1, 2, 5, 5, 6, 9]\n")


# Main

def main():
    check_correctness()

    datasets = generate_datasets()

    print("Sorting Performance (in ms)\n")
    print(f"{'Size':<8}{'Type':<10}{'Insertion':<15}{'Merge':<15}{'Quick':<15}")

    for (size, dtype), data in datasets.items():
        t1 = measure_time(insertion_sort, data)
        t2 = measure_time(merge_sort, data)
        t3 = measure_time(quick_sort, data)

        print(f"{size:<8}{dtype:<10}{t1:<15.2f}{t2:<15.2f}{t3:<15.2f}")

if __name__ == "__main__":
    main()