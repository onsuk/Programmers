from itertools import combinations

def solution(nums):
    return len(list(filter(is_prime, map(sum, combinations(nums, 3)))))

def is_prime(n):
    return factors(n) == [1, n]

def factors(n):
    return [x for x in range(1, n + 1) if n % x == 0]
