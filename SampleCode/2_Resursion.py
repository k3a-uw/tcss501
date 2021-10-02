def factorial(n):
    try:
        # base case
        if n < 0:
            return None
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    except TypeError:
        return None

def fact_lin(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i

    return ret

def fib_rec(n):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #recursive case
    else:
        return fib_rec(n-2)+fib_rec(n-1)

def fib_lin(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n2 = 0
        n1 = 1
        for i in range(1,n):
            ret = n2+n1
            n2 = n1
            n1 = ret
        return ret

    return tot

def fib_const(n):
    sq5 = 5**.5
    psi = (1 - sq5) / 2
    phi = (1 + sq5) / 2

    approx = (phi**n - psi**n) / sq5
    return int(approx)

def merge_sort(input_list):
    """
    Performs a classic merge sort, a linearithmic O(n log n) algorithm for soriting data.

    :param input_list A list of objects to be reversed.
    :return A sorted version/copy of the list.
    """

    if len(input_list) > 1:
        split = len(input_list) // 2
        left = input_list[:split]
        right = input_list[split:]
        left = merge_sort(left)
        right = merge_sort(right)

        output = []
        left_index = 0
        right_index = 0
        inst_c = 0
        while left_index < len(left) and right_index < len(right):
            inst_c += 1
            if left[left_index] < right[right_index]:
                output.append(left[left_index])
                left_index += 1
            else:
                output.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            output.append((left[left_index]))
            left_index += 1

        while right_index < len(right):
            output.append(right[right_index])
            right_index += 1

        return output
    return input_list


my_list = [1,5,4,3,4,5,3,2,1]

def palindrome(n):
    for i


def median(n):
    a_len = len(n)
    if(a_len) == 1:  # TRIVIAL CASE WHERE N IS A SINGLE VALUE
        return n[0]

    a = merge_sort(n)
    split = a_len // 2
    if a_len % 2 == 0:  # is even
        return (a[split-1] + a[split]) / 2
    else:
        return a[split]

l = [1,2,3,4,5]


def summary_stats(n):
    """

    :param n:
    :return:
    """

    # SEGMENT 1
    a_len = len(n)
    if a_len == 1:  # TRIVIAL CASE WHERE N IS A SINGLE VALUE
        return n[0], n[0]

    # SEGMENT 2
    a = merge_sort(n)  # USE WHAT YOU KNOW ABOUT TIME COMPLEXITY OF MERGE SORT FOR THIS SEGMENT

    # SEGMENT 3
    split = a_len // 2
    median: int = 0
    if a_len % 2 == 0:  # is even
        median = (a[split - 1] + a[split]) / 2
    else:
        median = a[split]

    # SEGMENT 4
    running_sum = 0
    for i in range(0, a_len):
        running_sum += a[i]

    mean = running_sum / a_len

    return (median, mean)
