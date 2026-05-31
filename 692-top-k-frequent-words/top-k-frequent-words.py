from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        x=Counter(words)
        y=[]
        for word in x:
            y.append((-x[word], word))
        y.sort()
        z=[]
        for i in range(k):
            z.append(y[i][1])
        return z