# Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
# To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as tuples ↴ of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

# For example:

#   (2, 3)  # meeting from 10:00 – 10:30 am
#   (6, 9)  # meeting from 12:00 – 1:30 pm

# Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges.

# For example, given:

# [[0, 1], [3, 5], [4, 8], [10, 12], [9, 10]]

# your function would return:

# [(0, 1), (3, 8), (9, 12)]


meetings = [[0, 1], [3, 5], [4, 8], [10, 12], [9, 10]]
# Initialize with at least the first meeting
merged_meetings = []

while True:
    merged = meetings.pop(0)
    
    while True:        
        i_overlap = [i for i, m in enumerate(meetings) if (merged[0]<=m[0]<=merged[1]) or (m[0]<=merged[0]<=m[1])]   
        
        if i_overlap:
            overlaped_meeting = meetings.pop(i_overlap[0])
            merged[0] = min(merged[0], overlaped_meeting[0])
            merged[1] = max(merged[1], overlaped_meeting[1])
        else:
            merged_meetings.append(merged)
            break
    
    if len(meetings) == 0:
        break

# This one was not correct, i should have assessed the time complexity earlier.
# There are 2 nested whiles that "kinda" iterate over the list, making it more like a O(n^2)
# Should have considered sorting

