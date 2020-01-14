def solution(n):
    battery = 0
    while(n > 0):
        battery += n % 2
        n = int(n / 2)
    return battery