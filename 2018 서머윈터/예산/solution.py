def solution(d, budget):
    d.sort()
    return can_supply(d, budget)


def can_supply(suppliable, budget):
    if sum(suppliable) <= budget:
        return len(suppliable)
    suppliable.pop()
    return can_supply(suppliable, budget)
