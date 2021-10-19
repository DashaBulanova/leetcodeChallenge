def backspace_compare(str1, str2):
    p1 = len(str1) - 1
    p2 = len(str2) - 1
    acc1 = 0
    acc2 = 0
    while p1 >= 0 or p2 >= 0:

        while p1 >= 0 and (str1[p1] == '#' or acc1 > 0):
            acc1 = acc1 + 1 if str1[p1] == '#' else acc1 - 1
            p1 -= 1

        while p2 >= 0 and (str2[p2] == '#' or acc2 > 0):
            acc2 = acc2 + 1 if str2[p2] == '#' else acc2 - 1
            p2 -= 1

        if p1 < 0 <= p2 or p2 < 0 <= p1:
            return False
        elif str1[p1] != str2[p2]:
            return False
        else:
            p1 -= 1
            p2 -= 1

    return True
