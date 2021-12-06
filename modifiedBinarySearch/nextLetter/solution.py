def nextGreatestLetter(letters, target) -> str:
    if len(letters) < 2:
        raise ValueError("input should have at least 2 letters")
    
    start, end = 0, len(letters)-1
    while start <= end:
        mid = start + int((end-start)/2)
        mid_letter = letters[mid]

        if mid_letter > target:
            #go to left
            end = mid - 1
        else:
            #go to right
            start = mid + 1

    return letters[start % len(letters)]