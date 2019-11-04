def solution(n):
    return rec(n)

def rec(n):
    if n == 1:
        return [0]
    return rec(n-1)+[0]+trans(rec(n-1))

def trans(lis):
    lis.reverse()
    return list(map(lambda x: int(not x), lis))


a = solution(3)
print(a)