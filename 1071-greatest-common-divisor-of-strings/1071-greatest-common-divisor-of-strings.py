class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        #find pattern
        pattern = ""
        temp_pattern = ""
        patterns = []
        for i in range(len(str2)):
            temp_pattern += str2[i]
            n = len(str2) // len(temp_pattern)
            if temp_pattern * n == str2:
                pattern = temp_pattern
                patterns.append(pattern)
        # pattern found.
        result = ""
        for i in range(len(patterns)):
            flag = True
            new_str1 = str1.split(patterns[i])
            for j in new_str1:
                if j != '':
                    flag = False
            if flag:
                result = patterns[i]
            else:
                continue
        return result