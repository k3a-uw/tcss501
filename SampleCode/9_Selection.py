def quick_select(arr, left, right, k):
    split = partition(arr, left, right)

    if split == k:
        return arr[split]
    elif split < k:
        return quick_select(arr, split + 1, right, k)
    else:
        return quick_select(arr, left, split - 1, k)


def partition(input_list, lower_idx, upper_idx):
    if lower_idx == upper_idx:
        return lower_idx

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


def get_index_of_nearest_median(arr, first, second, value):
    if first == second:
        return first
    else:
        return first + arr[first:second].index(value)


def med_of_meds(arr):
    sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]

    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist) // 2])

    if len(medians) <= 5:
        return sorted(medians)[len(medians) // 2]
    else:
        return med_of_meds(medians)


def partition_w_median(input_list, lower_idx, upper_idx):
    if lower_idx == upper_idx:
        return lower_idx

    nearest_median = med_of_meds(input_list[lower_idx: upper_idx])
    median_idx = get_index_of_nearest_median(input_list, lower_idx, upper_idx, nearest_median)

    tmp = input_list[lower_idx]
    input_list[lower_idx] = input_list[median_idx]
    input_list[median_idx] = tmp

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


def deterministic_select(arr, left, right, k):
    split = partition_w_median(arr, left, right)

    if split == k:
        return arr[split]
    elif split < k:
        return deterministic_select(arr, split + 1, right, k)
    else:
        return deterministic_select(arr, left, split - 1, k)


if __name__ == "__main__":
    my_array = [8, 6, 7, 5, 3, 0, 9]

    x = quick_select(my_array, 0, len(my_array)-1, 5)

    y = deterministic_select(my_array, 0, len(my_array) - 1, 5)