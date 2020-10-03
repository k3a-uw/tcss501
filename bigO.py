import random
import matplotlib.pyplot as plt
import numpy as np
import time




def array_reverse(input_list):
    """
    Reverses the elements of the list to demonstrate a linear algorithm of reversing an array of things.

    :param input_list A list of objects to be reversed.
    :return A returned version/copy of the list..
    """

    array_len = len(input_list)

    i = 0;

    output_list = [None] * array_len

    while i < array_len:
        output_list[i] = input_list[array_len-1 - i]
        i += 1

    return output_list


def bubble_sort(input_list):
    for i in range(0, len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[i] > input_list[j]:
                tmp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = tmp

    return input_list


def merge_sort(input_list):
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
    plt.ylabel("Steps to Complete")
    plt.xlabel("Input Size")
    plt.title(title)
    plt.ylim(0, max(y)*1.05)
    plt.plot(x, y, linestyle='--', marker='o')
    plt.show()


# RUN DIFFERING SAMPLES
MIN_SAMPLE_SIZE = 100
MAX_SAMPLE_SIZE = 10000
NUM_SAMPLES = 100

sample_sizes = np.linspace(MIN_SAMPLE_SIZE,
                           MAX_SAMPLE_SIZE,
                           NUM_SAMPLES,
                           dtype='int')

samples = []
for sample_size in sample_sizes:
    samples.append([random.randint(1, 100) for i in range(0, sample_size)])

runtimes = []
for sample in samples:
    print(f"Reversing {len(sample)} element array...", end="")
    start = time.perf_counter()
    r = array_reverse(sample)
    duration_seconds = time.perf_counter() - start
    runtimes.append(duration_seconds)
    print(f'{duration_seconds:0.00} seconds.', end="\r")

print("\nDONE")

draw_plot(sample_sizes, runtimes, "Linear Algorithm: Reverse")

instructions = []
for sample in samples:
    print(f"Bubble Sorting Array of len: {len(sample)}.")
    r, i = bubble_sort(sample)
    instructions.append(i)


draw_plot(sample_sizes, instructions, "Quadratic Algorithm: Bubble Sort")


samples = []
for sample_size in sample_sizes:
    samples.append([random.randint(1, 100) for i in range(0, sample_size)])

instructions = []
for sample in samples:
    print(f"Merge Sorting Array of len: {len(sample)}")
    r, i = merge_sort(sample)
    instructions.append(i)

draw_plot(sample_sizes, instructions, "n log n Algorithm: Merge Sort")

for sample in samples[0:len(samples)//2]):


