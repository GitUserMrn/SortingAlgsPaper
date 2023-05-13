import random
import time

g_v = 0

def generate_data(n):
    # Sets a fixed seed for the random number generator


    # Generates a list of n integers between 0 and 1000
    lst = list(range(n))
    # Yields the original list
    lst.reverse()
    yield lst

    # Performs additional shuffles to make the list random
    for i in range(3):
        random.shuffle(lst)
        yield lst



def bucketSort(array):
    global g_v
    g_v = 0
    # Create empty buckets
    bucket = [[] for _ in range(len(array))]

    # Insert elements into their respective buckets
    for j in array:
        g_v += 1
        index_b = int(10 * j / 1000000)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        g_v += 1
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            g_v += 1
            array[k] = bucket[i][j]
            k += 1
    return array

def bubble_sort(lst):
    n = len(lst)
    steps = 0
    for i in range(n):
        for j in range(n - i - 1):
            steps += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst, steps

def selection_sort(lst):
    n = len(lst)
    steps = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps += 1
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst, steps

def quick_sort(lst):
    steps = 0
    _quick_sort(lst, 0, len(lst) - 1, steps)
    return lst, steps

def _quick_sort(lst, start, end, steps):
    if start >= end:
        return lst, steps

    # Choose pivot element
    pivot_idx = (start + end) // 2
    pivot = lst[pivot_idx]

    # Move pivot to the end of the list
    lst[pivot_idx], lst[end] = lst[end], lst[pivot_idx]

    # Partition the list
    i = start
    for j in range(start, end):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        steps += 1

    # Move pivot back to its final position
    lst[i], lst[end] = lst[end], lst[i]
    steps += 1

    # Sort the two partitions
    _quick_sort(lst, start, i - 1, steps)
    _quick_sort(lst, i + 1, end, steps)

def merge_sort(lst):
    steps = 0
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            steps += 1
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            steps += 1
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            steps += 1
            lst[k] = right_half[j]
            j += 1
            k += 1

    return lst, steps

def heap_sort(lst):
    def heapify(lst, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and lst[i] < lst[l]:
            largest = l

        if r < n and lst[largest] < lst[r]:
            largest = r

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            heapify(lst, n, largest)

    n = len(lst)

    for i in range(n//2, -1, -1):
        heapify(lst, n, i)

    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst, 0

def counting_sort(lst):
    n = len(lst)
    k = max(lst) + 1
    count = [0] * k
    sorted_lst = [0] * n

    # Count the number of occurrences of each element in lst
    for i in range(n):
        count[lst[i]] += 1

    # Calculate the cumulative sum of count
    for i in range(1, k):
        count[i] += count[i-1]

    # Sort the elements in lst
    for i in range(n-1, -1, -1):
        sorted_lst[count[lst[i]]-1] = lst[i]
        count[lst[i]] -= 1

    return sorted_lst

def radix_sort(lst):
    # Determine the maximum number of digits in the largest element
    max_digits = len(str(max(lst)))

    # Iterate over each digit, from the least significant to the most significant
    for i in range(max_digits):
        # Create 10 buckets, one for each possible digit (0-9)
        buckets = [[] for _ in range(10)]

        # Distribute the elements of the list into the buckets based on the current digit
        for num in lst:
            digit = (num // (10 ** i)) % 10
            buckets[digit].append(num)

        # Rebuild the list by concatenating the elements in each bucket
        lst = [num for bucket in buckets for num in bucket]

    return lst


if __name__ == '__main__':
    fin_time = []
    fin_step = []
    data = generate_data(1000000)
    for i, lst in enumerate(data):
        print(f"List {i+1}: {lst[:100]}")
        start_time = time.time()
        sorted_lst = bucketSort(lst.copy())
        end_time = time.time()
        print(f"Number of steps: {g_v}")
        fin_step.append(g_v)
        print(f"Time: {end_time - start_time:.4f} seconds\n")
        time_i = round((end_time - start_time), 5)
        fin_time.append(time_i)

    print(f"Sorted list: {sorted_lst[:100]}\n")
    for i in fin_step:
        print(i)
    for i in fin_time:
        print(i)