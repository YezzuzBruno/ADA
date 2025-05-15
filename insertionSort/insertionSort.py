import time
import matplotlib.pyplot as plt
import random

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    numbers_worst_case = [10,9,8,7,6,5,4,3,2,1]
    print(numbers_worst_case)
    insertion_sort(numbers_worst_case)
    print(numbers_worst_case)

