def queen(cord_x1, cord_y1, cord_x2, cord_y2):
    if not cord_x1 or not cord_y1 or not cord_x2 or not cord_y2:
        return 'No'
    if cord_x1 == cord_x2 or cord_y1 == cord_y2:
        return 'Yes'
    elif abs(cord_x1 - cord_x2) == abs(cord_y1 - cord_y2):
        return 'Yes'
    else:
        return 'No'
