def solution(A, B):
    point = 0
    A.sort()
    B.sort()
    for a in A:
        for b in B:
            if(a < b): 
                B.remove(b)
                point += 1
                break
    return point