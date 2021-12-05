def search(input: list[int], key: int, l: int, r: int):
    if l == r:
        return l if input[l] == key else -1

    mid = l + int((r - l) / 2)
    left = search(input, key, l, mid)
    if left != -1:
        return left
    right = search(input, key, mid + 1, r)
    if right != -1:
        return right
    return -1


def search_key(input: list[int], key: int) -> int:
    return search(input, key, 0, len(input) - 1)
