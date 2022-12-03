class Solution:
	def frequencySort(self, s: str) -> str:
		fr = {}
		for c in s:
			fr[c]=fr.get(c, 0) + 1
		res = ''
		for k,v in sorted(fr.items(), key=lambda x: x[1], reverse=True):
			res += ''.join([k]*v)
		return res
