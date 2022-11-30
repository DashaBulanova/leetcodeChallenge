from typing import List

class Solution:
	def uniqueOccurrences(self, arr: List[int]) -> bool:
		map = {}
		for i in arr:
			map[i]=map.get(i,0) + 1
		
		return len(set(map.values()))==len(map)
