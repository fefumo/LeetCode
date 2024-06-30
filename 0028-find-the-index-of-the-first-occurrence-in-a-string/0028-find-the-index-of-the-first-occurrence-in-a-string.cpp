class Solution {
public:
    int strStr(string haystack, string needle) {
        int nlen = needle.length();
        int hlen = haystack.length();
        for (int i = 0; i <= hlen-nlen; ++i){
            if (haystack.substr(i, nlen) == needle){
                return i;
            }
        }
        return -1;
    }
};