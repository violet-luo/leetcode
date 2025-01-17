def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals.sort(key = lambda interval:interval[0])
    meetings = []
    room = 0

    for start, end in intervals:
        if room == 0: 
            meetings.append(end)
            room += 1 
        # existing room becomes available: the earliest end time in meetings < start
        elif min(meetings) <= start: 
            meetings.remove(min(meetings))
            meetings.append(end)
        else: 
            room += 1 
            meetings.append(end)

    return room
