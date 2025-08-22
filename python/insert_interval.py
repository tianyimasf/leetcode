"""
Pseudo code:
(this method only update the list and not actually insert)
- initialize an empty list.
- check the list of start_i one by one until find one that's equal
    or larger than start. add each of the prev intervals to the
    empty list.
- check end_i, if end_i less or equal than end, update end_i = end
- check end_(i+1), if end_(i+1) less or equal than end, move to the
    next interval, until find one interval j where end_j > end.
- check if start_j = start. if so, update end_i = end_j and add all
    intervals after interval j to the new list. if not, add both 
    interval_j and every interval after to the new list.
- return the new list.

ex. [[1,2],[3,5],[6,7],[8,10],[12,16]]

"""

def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    new_intervals = []
    merged = False
    start, end = newInterval[0], newInterval[1]
    lastIdx = 0

    for idx, interval in enumerate(intervals):
        # if the new interval is merged, break and add the rest of the
        # intervals from the list
        if merged: break
        start_i, end_i = interval[0], interval[1]
        start_ip1, end_ip1 = intervals[idx+1][0], intervals[idx+1][1] # "p1" stands for "plus 1"
        # if start of the new interval is larger than the start of the current and next interval, 
        # simply append interval
        if start >= start_i and start > start_ip1:
            new_intervals.append(interval)
        # else if the start of the interval is between the start of the current and next interval
        elif start >= start_i and start <= start_ip1: 
            # if the start of the next interval is larger than start, start merging
            # if the end of the current interval is smaller than the start of the new interval, 
            # then the current interval overlaps with the new interval. Merge the two.
            newEnd = end
            if start <= end_i: 
                start = start_i
                if end < start_ip1: 
                    lastIdx = idx + 1
                    merged = True
                    new_intervals.append([start, end])
                    continue
            # if the start of the new interval do not overlap with the current interval
            # keep the start of the new interval as is and start checking the end of it
            # if the end of the new interval is larger than the next interval, merge the two until
            # the end of the new interval is smaller than the start of the next interval and thus
            # do not overlap with the next interval
            while end >= start_ip1:
                newEnd = end_ip1
                idx += 1
                start_ip1, end_ip1 = intervals[idx][0], intervals[idx][1]
            merged = True
            lastIdx = idx
            # append the new interval
            new_intervals.append([start, newEnd])
    new_intervals.extend(intervals[lastIdx:])
    return new_intervals

# Test 1
newInterval = [4,8]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_intervals = insert(intervals, newInterval)
print("Question", intervals, ", new interval: ", newInterval, "\nAnswer: ", new_intervals) # [[1,2],[3,10],[12,16]]

# Test 2
newInterval = [2, 5]
intervals = [[1,3],[6,9]]
new_intervals = insert(intervals, newInterval)
print("Question", intervals, ", new interval: ", newInterval, "\nAnswer: ", new_intervals) # [[1,5],[6,9]]