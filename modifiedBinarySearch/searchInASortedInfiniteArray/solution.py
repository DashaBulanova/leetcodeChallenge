import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def search_in_infinite_array(reader, key):
    n = 0
    start = 0
    end = pow(2, n)
    while start <= end:
        if start == end:
            return start if reader.get(start) == key else -1
        mid = start + int((end-start)/2)
        mid_item = reader.get(mid)

        if mid_item == key:
            return mid
        if mid_item == math.inf:
            n -= 0.5
            end = int(pow(2, n))
        elif mid_item > key:
            end = mid-1
        else:
            start = mid+1
            n+=1
            end = int(pow(2, n))

    return -1