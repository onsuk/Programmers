def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    d.sort()
    d.pop()
    return solution(d, budget)
