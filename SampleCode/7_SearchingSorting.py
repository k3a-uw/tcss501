

def linear_search(haystack, needle):
    found = False
    for element in haystack:
        found = (element == needle)
        if found:
            print(f"Found: {needle}!")
            break

    if not found:
        print(f"Counldn't find {needle}. :-(")

    return found


def linear_search_concise(haystack, needle):
    for element in haystack:
        if element == needle:
            return element
    return None


def linear_search_from_book(unordered_list, term):
    for i in range(len(unordered_list)):
        if term == unordered_list[i]:
            return unordered_list[i]
    return None


def linear_search_ordered(haystack, needle):
    found = False
    for element in haystack:
        found = (element == needle)
        if found:
            print(f"Found {needle}!")
        elif needle > element:
            break

    if not found:
        print(f"Counldn't find {needle}. :-(")

    return found


def linear_search_ordered_concise(haystack, needle):
    for element in haystack:
        if element == needle:
            return element
        elif needle > element:
            break

    return None


def linear_search_ordered_book(ordered_list, term):
    for i in range(len(ordered_list)):
        if term == ordered_list[i]:
            return i
        elif term > ordered_list[i]:
            return None
    return None


def binary_search(haystack, needle):
    lower_idx = 0
    upper_idx = len(haystack) - 1

    while lower_idx <= upper_idx:
        midpoint = (upper_idx + lower_idx) // 2
        if haystack[midpoint] == needle:
            print(f"Found {needle} at index {midpoint}")
            return True
        if needle > haystack[midpoint]:
            lower_idx = midpoint + 1
        else:
            upper_idx = midpoint - 1

    print(f"Count Not Find {needle} :-(")
    return False


def binary_search_recursive(haystack, needle, lower_idx, upper_idx):
    if upper_idx < lower_idx:
        return None
    else:
        midpoint = (lower_idx + upper_idx) // 2
        if haystack[midpoint] == needle:
            return midpoint
        elif needle > haystack[midpoint]:
            return binary_search_recursive(haystack, needle, midpoint+1, upper_idx)
        else:
            return binary_search_recursive(haystack, needle, lower_idx, midpoint-1)


def interpolation_search(haystack, needle):
    lower_idx = 0
    upper_idx = len(haystack) - 1

    while lower_idx <= upper_idx:
        midpoint = nearest_mid(haystack, needle, lower_idx, upper_idx)

        if midpoint > upper_idx or midpoint < lower_idx:
            return None
        if haystack[midpoint] == needle:
            print(f"Found {needle} at index {midpoint}")
            return True

        if needle > haystack[midpoint]:
            lower_idx = midpoint + 1
        else:
            upper_idx = midpoint - 1

    print(f"Could not find {needle} :-(")
    return False


def nearest_mid(haystack, needle, lower_idx, upper_idx):
    idx_range = upper_idx - lower_idx
    val_range = haystack[upper_idx] - haystack[lower_idx]
    idx_val_ratio = idx_range / val_range
    search_distance = needle - haystack[lower_idx]
    search_offset = search_distance * idx_val_ratio

    return int (lower_idx + search_offset)


def bubble_sort(input_list):
    for i in range(1, len(input_list)):
        for j in range(len(input_list) - i):
            if input_list[j] > input_list[j+1]:
                tmp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = tmp

    return input_list


def insertion_sort(input_list):
    for i in range(1,len(input_list)):
        tmp = input_list[i]
        j = i-1

        while tmp < input_list[j] and j>= 0:
            input_list[j+1] = input_list[j]
            j -= 1

        input_list[j+1] = tmp

    return input_list


def selection_sort(input_list):
    for i in range(0, len(input_list) - 1):
        for j in range(i+1, len(input_list)):
            if input_list[j] < input_list[i]:
                tmp = input_list[j]
                input_list[j] = input_list[i]
                input_list[i] = tmp
    return input_list


def partition(input_list, lower_idx, upper_idx):
    pivot = input_list[lower_idx]
    pivot_index = lower_idx
    right_idx = upper_idx
    left_idx = lower_idx + 1

    while True:
        while input_list[left_idx] < pivot and left_idx < upper_idx:
            left_idx += 1

        while input_list[right_idx] > pivot and right_idx >= lower_idx:
            right_idx -= 1

        if left_idx < right_idx:
            temp = input_list[left_idx]
            input_list[left_idx] = input_list[right_idx]
            input_list[right_idx] = temp
        else:
            break

    input_list[pivot_index] = input_list[right_idx]
    input_list[right_idx] = pivot
    return right_idx


def quick_sort(input_list, first, last):
    if last - first <= 0:
        return None
    else:
        partition_point = partition(input_list, first, last)
        quick_sort(input_list, first, partition_point - 1)
        quick_sort(input_list, partition_point + 1, last)




import random
random.seed(100)

ARRAY_SIZE = 32
LOW_NUM = 1
HIGH_NUM = ARRAY_SIZE * 5

my_list = []
for i in range(32):
    my_list.append(random.randint(LOW_NUM, HIGH_NUM))


quick_sort(my_list, 0, len(my_list) - 1)
