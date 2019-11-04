def solution(w,h):
    return (w * h) - (w + h - gcm(w, h))

def gcm(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a
