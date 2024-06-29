class Solution {
public:
    int strStr(string haystack, string needle) {
        int res = haystack.find(needle) >=0 ? haystack.find(needle) : -1;
        return res;
    }
};