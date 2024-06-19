class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        arr = []
        for i in magazine:
            arr.append(i)
        
        for letter in ransomNote:
            if letter not in arr:
                return False
            arr.remove(letter)
        return True