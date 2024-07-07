class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r = ""
        for i in range(len(s)):
            n = (i + k + len(s)) % len(s)
            r += s[n]
        return r

