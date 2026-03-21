class Solution(object):
    def findWordsContaining(self, words, x):
        n=[]
        for i in range(len(words)):
            if x in words[i]:
                n.append(i)
        return n

        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        