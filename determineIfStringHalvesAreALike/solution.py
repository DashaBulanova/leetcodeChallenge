class Solution:
	def halvesAreAlike(self, s: str) -> bool:
		a_count = 0
		b_count = 0
		volwels = set(['a', 'e', 'i', 'o', 'u'])
		i=0
		halve = int(len(s)/2)
		while i < halve:
			if s[i].lower() in volwels:
				a_count += 1
			if s[i+halve].lower() in volwels:
				b_count += 1
			i+=1
		return a_count == b_count
			
