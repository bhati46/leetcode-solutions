class Solution:
    def frequencySort(self, s: str) -> str:
        x=Counter(s)
        s=""
        for ch,freq in x.most_common():
            s+=ch*freq
        return s