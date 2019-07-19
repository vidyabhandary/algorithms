# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:44:25 2019

@author: Vidya
"""


def mergesort_inversions(array):

    if len(array) < 2:
        return array, 0

    mid = int(len(array) / 2)

    left, left_i = mergesort_inversions(array[:mid])
    right, right_i = mergesort_inversions(array[mid:])

    i = j = 0
    merged = []

    inversion_count = 0 + left_i + right_i

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            inversion_count += len(left[i:])

            a = i
            b = j

            while a < len(left):
                print('-(', left[a], right[b], ')-', end='')
                a += 1

            merged.append(right[j])
            j += 1

    if i < len(left):
        merged += left[i:]
    else:
        merged += right[j:]

    return merged, inversion_count


def bruteforce_inversions(arr):
    inv_count = 0
    n = len(arr)

    for r in range(n):
        for s in range(r + 1, n):
            if arr[r] > arr[s]:
                inv_count += 1
                print('*(', arr[r], arr[s], ')*', end='')

    return inv_count


if __name__ == '__main__':

    array1 = [5, 1, 4, 9, 2, 6, 8, 3, 5]
    print('Merge Sort Inversion Pairs- 1')
    sorted_array, total_inversions = mergesort_inversions(array1)

    # Expected Result - [1, 2, 3, 4, 5, 5, 6, 8, 9]
    # Expected Result - Total Inversions = 15
    print('\nSorted Array ', sorted_array)
    print('Total Inversions in Array --> ', total_inversions)

    # Total Inversions = 15
    print('\nBrute Force Inversion - 1')
    print('\nTotal Inversion counted using bruteforce --> ',
          bruteforce_inversions(array1))

    print('-' * 50)
    array2 = [2, 4, 6, 1, 3, 5]
    print('\nMerge Sort Inversion Pairs - 2')
    sorted_array, total_inversions = mergesort_inversions(array2)

    # Expected Result - [1, 2, 3, 4, 5, 6]
    # Expected Result - Total Inversions = 6
    print('\nSorted Array ', sorted_array)
    print('Total Inversions in Array --> ', total_inversions)

    # Expected Result - Total Inversions = 6
    print('\nBrute Force Inversion - 2')
    print('\nTotal Inversion counted using bruteforce --> ',
          bruteforce_inversions(array2))

    print('-' * 50)
    array3 = [1, 3, 5, 2, 4, 6]
    print('Merge Sort Inversion Pairs - 3')
    sorted_array, total_inversions = mergesort_inversions(array3)

    # Expected Result - [1, 2, 3, 4, 5, 6]
    # Expected Result - Total Inversions = 3
    print('\nSorted Array ', sorted_array)
    print('Total Inversions in Array --> ', total_inversions)

    # Expected Result - Total Inversions = 3
    print('\nBrute Force Inversion - 3')
    print('\nTotal Inversion counted using bruteforce --> ',
          bruteforce_inversions(array3))

    print('-' * 50)

    array4 = [7676, 175, 400, 999, 2, 60, 811, 13, 378]
    print('Merge Sort Inversion Pairs - 4')
    sorted_array, total_inversions = mergesort_inversions(array4)

    # Expected result - [2, 13, 60, 175, 378, 400, 811, 999, 7676]
    # Expected Result - Total Inversions = 23
    print('\nSorted Array ', sorted_array)
    print('Total Inversions in Array --> ', total_inversions)

    # Expected Result - Total Inversions = 23
    print('\nBrute Force Inversion - 4')
    print('\nTotal Inversion counted using bruteforce --> ',
          bruteforce_inversions(array4))
