class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals):
        end_time = -1
        for interval in sorted(intervals, key = lambda interval: interval.start):
            if interval.start < end_time:
                return False
            end_time = interval.end 
        return True
