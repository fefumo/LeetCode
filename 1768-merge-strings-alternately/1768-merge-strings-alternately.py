class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ra = 0
        s = ""
        first = False
        second = False
        if len(word1) >= len(word2):
            ra = len(word2)
            first = True
        else:
            ra = len(word1)
            second = True
        for i in range(ra):
            s += word1[i]
            s += word2[i]
            
        if first:
            s += word1[ra:]
        else:
            s += word2[ra:]
            
        return s