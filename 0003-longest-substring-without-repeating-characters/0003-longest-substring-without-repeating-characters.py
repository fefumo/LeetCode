class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if len(s) == 0: return 0;
        for i in range(len(s)):
            visited = set()
            for j in range(i,len(s)):
                if s[j] in visited:
                    break
                else:
                    res = max(res, j - i + 1)
                    visited.add(s[j])
        return res