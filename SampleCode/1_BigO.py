import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import sys

MIN_SAMPLE_SIZE = 100
MAX_SAMPLE_SIZE = 100000
NUM_SAMPLES = 100

sample_sizes = np.linspace(MIN_SAMPLE_SIZE,
                           MAX_SAMPLE_SIZE,
                           NUM_SAMPLES,
                           dtype='int')

# THIS MAY TAKE SOME TIME ON SLOWER MACHINES YOU CAN REDUZE THE NUMBER OF SAMPLES OR SAMPLE SIZE ABOVE
samples = []
for sample_size in sample_sizes:
    samples.append([random.randint(1, 100) for i in range(0, sample_size)])

print("The below list shows the various sample sizes created for this test.")
print(sample_sizes)


#### BEGIN FUNCTION DEFINITIONS ####
def array_reverse(input_list):
    """
    Reverses the elements of the list to demonstrate a linear algorithm of reversing an array of things.

    :param input_list A list of objects to be reversed.
    :return A returned version/copy of the list.
    """

    array_len = len(input_list)

    i = 0;

    output_list = [None] * array_len

    while i < array_len:
        output_list[i] = input_list[array_len-1 - i]
        i += 1

    return output_list


def bubble_sort(input_list):
    """
    Compare each element with each other element to provide a sorted array.

    :param input_list A list of objects to be reversed.
    :return A sorted version/copy of the list.
    """

    for i in range(0, len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                tmp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = tmp

    return input_list


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


def draw_plot(x, y, title="My Cool Chart"):
    """
    A simple helper function that uses matplotlib to plot the provided x and y vectors, and applies
    the provided title.

    :param x A list of values to be plotted on the x axis (must be same length (or factor of x))
    :param y A list of values to be plutted on the y axis (must be same length (or factor of x))
    :title title The title to display at the top of the chart.
    """
    plt.ylabel("Steps to Complete")
    plt.xlabel("Input Size")
    plt.title(title)
    plt.ylim(0, max(y) * 1.05)
    plt.plot(x, y, linestyle='--', marker='o')
    plt.show()


#### END FUNCTION DEFINITIONS ####

#### BEGIN EMPIRICAL ANALYSIS ####

runtimes = []
tot_start = time.perf_counter()
for sample in samples:
    start = time.perf_counter()
    r = array_reverse(sample)
    duration_seconds = time.perf_counter() - start
    runtimes.append(duration_seconds)
    print(f"Reversed the {len(sample)} element array in {duration_seconds:.2f} seconds.", end="\r")

tot_duration_seconds = time.perf_counter() - tot_start
print(f"\n\nTest Complete, Total Duration: {tot_duration_seconds:.2f} seconds.")

draw_plot(sample_sizes, runtimes, "Linear Algorithm O(n): Reverse")


runtimes = []
tot_start = time.perf_counter()
for sample in samples:
    start = time.perf_counter()
    r = merge_sort(sample)
    duration_seconds = time.perf_counter() - start
    runtimes.append(duration_seconds)
    print(f"Merge Sorted the {len(sample)} element array in {duration_seconds:.2f} seconds.", end="\r")

tot_duration_seconds = time.perf_counter() - tot_start
print(f"\n\nTest Complete, Total Duration: {tot_duration_seconds:.2f} seconds.")

draw_plot(sample_sizes, runtimes, "N log N Algorithm O(n log(n)): Merge Sort")


runtimes = []
tot_start = time.perf_counter()
for sample in samples[0:10]:
    start = time.perf_counter()
    r = bubble_sort(sample)
    duration_seconds = time.perf_counter() - start
    runtimes.append(duration_seconds)
    print(f"Bubble Sorted the {len(sample)} element array in {duration_seconds:.2f} seconds.", end="\r")

tot_duration_seconds = time.perf_counter() - tot_start
print(f"\n\nTest Complete, Total Duration: {tot_duration_seconds:.2f} seconds.")

draw_plot(sample_sizes[0:10], runtimes, "Polynomial Time Algorithm O(n^2): Bubble Sort")



def summary_stats(n):
    """ First calculates the median, and then the average.
    :param n: An array of numeric values.
    :return: A tuple of (median,average)
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


l = [1,7,4,2,1,4,3,6,7,3,12,40]
med, avg = summary_stats(l)

print("Hello World, Example")