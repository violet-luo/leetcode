def get_bad_access(records):
    no_exit = set()
    no_enter = set()
    room = set()

    for name, swipe in records:
        if swipe == 'enter':
            if name in room:
                no_exit.add(name)
            else:
                room.add(name)
        elif swipe == 'exit':
            if name not in room:
                no_enter.add(name)
            else:
                room.discard(name)
    
    for person in list(room):
        no_exit.add(person)
        
    return no_exit, no_enter
