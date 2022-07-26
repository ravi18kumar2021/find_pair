# Find a pair with a minimum absolute sum in an array

'''
Given a sorted integer array, find a pair in it having an absolute
minimum sum.

input A = [-6, -5, -3, 0, 2, 4, 9]
output --- pair is (-5,4)
(-5,4) = abs(-5+4) = abs(-1) = 1, which is minimum among all pairs

to maintain search space by maintaing two indexes (low and high)
that initially points to two endpints of the array. Then loop
if low is less than high index and reduce the search space arr[low..high]
at each iteration of the loop by comparing the sum of elements
present at index low and high with 0.
We increment index low if the sum is less than 0 otherwise,
decrement index high if the sum is more than the 0.
We also maintain the minimum absolute difference among 
all pairs present at low and high index.
'''

import sys

# function to find a pair in a list with an absolute minimum sum
def find_pair(array):
    if len(array) < 2:
        return

    # sort the list if it is unsorted
    # maintain two indexes pointing to endpoints of the list
    (low, high) = (0, len(array) - 1)

    # min variable stores the minimum absolute difference
    min = sys.maxsize
    i = j = 0

    # reduce the search space array[low_high] at each iteration of the loop
    # loop if low is less than high variable
    while low < high:
        # update the minimum if the current absolute sum is less 
        if abs(array[high] + array[low]) < min:
            min = abs(array[high] + array[low])
            (i, j) = (low, high)

        # optimization pair with zero sum is found
        if min == 0:
            break

        # increment low index if the total is less than 0:
        # decrement high index if the total is more than 0
        if array[high] + array[low] < 0:
            low = low + 1
        else:
            high = high - 1

    # print the pair
    print("Pair found",(array[i], array[j]))

if __name__=='__main__':
    A = [-6, -5, -3, 0, 2, 4, 9]
    find_pair(A)