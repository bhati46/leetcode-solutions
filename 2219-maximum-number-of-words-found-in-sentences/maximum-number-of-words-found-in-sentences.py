class Solution(object):
    def mostWordsFound(self, sentences):
        max=0
        for i in sentences:
            x=len(i.split())
            if x>max:
                max=x
        return max
        """
        :type sentences: List[str]
        :rtype: int
        """
        