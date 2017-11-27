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

# Sorting n*log(n)
meetings.sort(key = lambda m:m[0])

merged = [meetings[0]]

for meeting_start, meeting_end in meetings[1:]:
    # Can we merge with previous?
    prev_meeting_start, prev_meeting_end = merged[-1]
    
    # Conditions to check if meetings can merge
    # prev_meeting[0] <= meeting[0] <= prev_meeting[1]
    if(prev_meeting_start <= meeting_start <= prev_meeting_end):
        merged[-1] = [prev_meeting_start,max(prev_meeting_end, meeting_end)]
    else:
        merged.append([meeting_start,meeting_end])
        
# Turned out nice and clean, with n*log(n) complexity