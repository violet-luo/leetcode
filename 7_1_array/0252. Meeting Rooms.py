def canAttendMeetings(self, intervals):
    intervals.sort(key = lambda interval:interval[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True
