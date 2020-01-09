def solution(dirs):
    handled_out_of_range = ignore_out_of_range(dirs)
    handled_visit_twice = ignore_visit_twice(handled_out_of_range)
    return len(set(frozenset(i) for i in handled_visit_twice))

def ignore_out_of_range(dirs):
    res = []
    current = (0, 0)
    for dir in dirs:
        if(dir == 'L'):
            if(current[0] == -5): continue
            current = (current[0] - 1, current[1])
        elif(dir == 'R'):
            if(current[0] == 5): continue
            current = (current[0] + 1, current[1])
        elif(dir == 'D'):
            if(current[1] == -5): continue
            current = (current[0], current[1] - 1)
        elif(dir == 'U'):
            if(current[1] == 5): continue
            current = (current[0], current[1] + 1)
        res.append(dir)
    return res

def ignore_visit_twice(dirs):
    res = []
    current = (0, 0)
    for dir in dirs:
        if(dir == 'U'):
            moved = (current[0], current[1]+1)
            res.append([current, moved])
            current = moved
        elif(dir == 'D'):
            moved = (current[0], current[1]-1)
            res.append([current, moved])
            current = moved
        elif(dir == 'R'):
            moved = (current[0]+1, current[1])
            res.append([current, moved])
            current = moved
        elif(dir == 'L'):
            moved = (current[0]-1, current[1])
            res.append([current, moved])
            current = moved
    return res