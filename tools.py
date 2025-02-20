def check_class_clash(timetable, day_time):
    #Checks if the given slots are already occupied by another course.

    day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}
    time_map = {'8:00': 0, '9:00': 1, '10:00': 2, '11:00': 3, '12:00': 4, '13:00': 5, '14:00': 6, '15:00': 7}

    clashes = [] #will use to store the day-time pairs where clashes occur

    for day, time in day_time:
        row, col = day_map[day], time_map[time]
        if timetable[row][col]: 
            clashes.append((day, time))  # Clash found

    return clashes  


#list of tuples of the form (day, time)
def add_class_to_schedule(timetable, day_time, course):

    day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4}
    time_map = {'8:00': 0, '9:00': 1, '10:00': 2, '11:00': 3, '12:00': 4, '13:00': 5, '14:00': 6, '15:00': 7}

    clashes = check_class_clash(timetable, day_time)
    if clashes:
        print(f'Cannot add {course} ! Clashes detected on :\n')
        for day, time in clashes:
            print(f'{day} and at {time}\n')

        return
    
    else:
        for day, time in day_time:
            row, col = day_map[day], time_map[time]
            timetable[row][col] = course

            print(f'{course} added on {day} at {time} !')



def remove_class_from_schedule(timetable, course):
    removed = False  # Flag to track course 

    for row in range(len(timetable)):  
        for col in range(len(timetable[0])):  
            if timetable[row][col] == course:
                timetable[row][col] = ''  
                removed = True

    if removed:
        print(f"All occurrences of {course} have been removed from the schedule.")
    else:
        print(f"{course} was not found in the schedule.")



def check_class_taken(completed_courses, course_code):
    if course_code in completed_courses:
        print(f"{course_code} has already been taken.")
        return True
    else:
        print(f"{course_code} has not been taken yet.")
        return False
