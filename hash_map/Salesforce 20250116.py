def max_swipes(logs):
    # Dictionary to store timestamps for each person
    swipe_logs = defaultdict(list)
    
    # Populate swipe_logs with timestamps per person
    for person, time in logs:
        swipe_logs[person].append(int(time))  # Convert time to integer for comparison
    
    max_swipes = 0
    max_person = None
    
    # Iterate over each person's swipe times
    for person, times in swipe_logs.items():
        times.sort()  # Ensure the times are sorted
        left = 0
        max_count = 0
        
        # Sliding window approach
        for right in range(len(times)):
            while times[right] - times[left] > 100:  # Keep window within a 1-hour range
                left += 1
            
            max_count = max(max_count, right - left + 1)
        
        # Track the person with max swipes
        if max_count > max_swipes:
            max_swipes = max_count
            max_person = person
    
    return max_person, max_swipes
