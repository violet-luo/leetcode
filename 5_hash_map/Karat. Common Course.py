def courseOverlaps(enrollment):
    courses = {}
    res = {}
    
    for student_id, course in enrollment:
        if student_id in courses:
            courses[student_id].append(course)
        else:
            courses[student_id] = [course]

    student_id = list(courses.keys())
    for i in range(len(student_id)):
        for j in range(i + 1, len(student_id)):
            overlaps = []
            for course1 in courses[student_id[i]]:
                for course2 in courses[student_id[j]]:
                    if course1 == course2:
                        overlaps.append(course1)
            students = (student_id[i], student_id[j])
            res[students] = overlaps
    return res
