# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:11:21 2019

@author: Vidya
"""


def merge(array1, array2):
    i = j = 0
    merged = []
    len_ar1 = len(array1)
    len_ar2 = len(array2)

    while i < len_ar1 and j < len_ar2:
        if array1[i] < array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1

    if i < len_ar1:
        merged += array1[i:]
    else:
        merged += array2[j:]

    return merged


def mergesort(array):

    if len(array) < 2:
        return array[:]

    mid = int(len(array) / 2)
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])

    return merge(left, right)


if __name__ == '__main__':

    # Duplicate values
    # Expected result - [1, 2, 3, 4, 5, 5, 6, 8, 9]
    print(mergesort([5, 1, 4, 9, 2, 6, 8, 3, 5]))

    # Bigger numeric values
    # Expected result - [2, 13, 60, 175, 378, 400, 811, 999, 7676]
    print(mergesort([7676, 175, 400, 999, 2, 60, 811, 13, 378]))

    # Empty list
    # Expected result - []
    print(mergesort([]))

    # Sorted list
    # Expected result - [1, 2, 3, 4, 5]
    print(mergesort([1, 2, 3, 4, 5]))

    # Same number through out
    # Expected result - [7, 7, 7, 7, 7]
    print(mergesort([7, 7, 7, 7, 7]))

    # Checking assertion
    # Expected result - No Assertion error
    assert(mergesort([3, 2, 0, 1]) == [0, 1, 2, 3]), 'MergeSort not working'
