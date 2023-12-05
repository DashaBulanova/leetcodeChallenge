class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        d = {}
        for c in chars:
            d[c] = d.get(c, 0) + 1
        
        result = 0
        for word in words:
            w = {}
            for ch in word:
                w[ch] = w.get(ch, 0)+1
            good=True
            for k, v in w.items():
                if k in d and v <= d[k]:
                    continue
                else:
                    good=False
                    break
            if good:
                result += len(word)
        return result
        
