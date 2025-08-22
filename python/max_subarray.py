"""
Pseudo-code

- have a right and a left pointer that both start at the left. 
- the right pointer move to the right most element, calculating
the sum of each subarray
- once the right pointer reaches the right, the left pointer start
moving to the right most element, calculating the sum of each sub-
array between the two pointers. 
- while moving the pointers, keep track of the max sum calculated.
- return the sum in the end.

Question: is this the best way to move the two pointers? can I move
the pointers more optimally?
Thoughts: it should not, since the left pointer stays at the left, 
and the right pointer stays at the right in the second pass. However,
Maybe not all cases are covered, for example the case when the subarray
is fully enclosed in the array. To cover the in-between cases, we should
just iterate through 1-n for the two pointers, but use dynamic pro-
gramming to save compute time. 

Edge case: should ignore when i = j = 0 and i = j = n

Correction: actually we can just move the left pointer to the right for 1
after the right pointer reaches the end and reset the right pointer.
"""

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1: return nums[0]
    cache = n * [n * [None]]
    sum = float("-inf")
    for i in range(n):
        cache[i][i] = nums[i] # initialization
        if cache[i][i] > sum: sum = cache[i][i]
        for j in range(i+1, n):
            cache[i][j] = cache[i][j-1] + nums[j]
            if cache[i][j] > sum: sum = cache[i][j]
    return sum

example_nums = [-2,1]
solution = maxSubArray(example_nums)
print(solution)

"""
Reflection: the execution was correct, but the initialization was incorrect. 
            for every new row, there needs to be a new initialization. My program
            got it wrong first because I only initialized for the first element
            on the first row, then because I only initialized for the first row.

            the second mistake is forget to consider the edge case where len(array) = 1.
            and when len(array) = 2, the answer should just be max(array[0], array[1], sum(array)).
            Things to remember: always consider the cases when len(array) is small (1 or 2)

            Actually scratch that, the real mistake is didn't think of a single element
            as a subarray as well.
"""


        