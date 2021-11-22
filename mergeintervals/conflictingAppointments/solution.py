def has_overlapping(a, b):
	if a[0]<a[1]<=b[0]<b[1]:
		return False
	return True

def can_attend_all_appointments(intervals):
  if len(intervals) < 2:
  	return True

  intervals.sort(key=lambda x: x[0])

  for i in range(1, len(intervals)):
  	if has_overlapping(intervals[i-1], intervals[i]):
  		return False

  return True