from collections import deque

def segment(x, space):
    start = 0
    segments = []
    deque =
    for end in range(space - 1, len(x)):
        segments.append(x[start:end + 1])
        start += 1

    acc = -1
    for seg in segments:
        acc = max(min(seg), acc)

    return acc
