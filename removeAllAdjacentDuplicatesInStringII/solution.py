from collections import deque

class Solution:
	def removeDuplicates(self, s: str, k: int) -> str:
		queue = deque()
	
		for i in s:
			if not queue:
				queue.append([i, 1])
			else:
				prev = queue[-1]
				if prev[0] == i:
					queue.pop()
					if prev[1]+1<k:
						queue.append([i, prev[1]+1])
				else:
					queue.append([i, 1])
		res = []			
		for k, v in list(queue):
			for i in range(v):
				res.append(k)
		return ''.join(res)
