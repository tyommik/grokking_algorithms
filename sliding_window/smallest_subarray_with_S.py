"""
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray
whose sum is greater than or equal to ‘S’.
Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

"""
import math

def my_smallest_subarray_with_given_sum(s, arr):
    step = 0
    solution = []
    while step <= len(arr):
        for i in range(len(arr) - step):
            subarray = arr[i:i + step + 1]
            if sum(subarray) >= s:
                solution.append(arr[i:i + step + 1])
        if len(solution):
            break
        step += 1
    return 1 + step

def smallest_subarray_with_given_sum(s, arr):
    windowSum = 0
    window_start = 0
    minLength = math.inf
    for window_end in range(0, len(arr)):
        windowSum += arr[window_end]
        while windowSum >= s:
            minLength = min(minLength, window_end - window_start + 1)
            windowSum -= arr[window_start]
            window_start += 1
    if minLength == math.inf:
        return 0
    return minLength


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(100, [3, 4, 1, 1, 6])))


if __name__ == '__main__':
    main()