# 19번 테스트 케이스를 통과하지 못함.

from math import ceil
from collections import Counter

def solution(n, words):
    if is_duplicated(words):
        return result(duplicated_index(words), n)

    check, last_words, first_words = is_wrong(words)
    if check:
        return result(wrong_index(last_words, first_words), n)
    
    return [0, 0]

def is_duplicated(words):
    return not(Counter(words) == Counter(list(set(words))))

def duplicated_index(words):
    return [i for i, word in enumerate(words) if word == duplicated_word(words)][1]

def duplicated_word(words):
    return { words.count(x): x for x in words }.get(2)

def is_wrong(words):
    last_words = list(map(lambda x: x[-1], words))[:-1]
    first_words = list(map(lambda x: x[0], words))[1:]
    return (not(last_words == first_words), last_words, first_words)

def wrong_index(last_words, first_words):
    return [i for i, word in enumerate(last_words) if not(word == first_words[i])][0] + 1

def result(index, n):
    return [(index % n) + 1, ceil((index + 1) / n)]
