class Solution {
public:
    int minimumDeletions(string s) {
        vector<int> pref_b(s.size());
        vector<int> suf_a(s.size());
        int a_count = count(s.begin(), s.end(), 'a');
        suf_a[0] = a_count;
        
        if (s[0] == 'b') pref_b[0] = 1;
        else pref_b[0] = 0;
                
        for (int i = 1; i < s.size(); i++){
            if(s[i] == 'b'){
                pref_b[i] = pref_b[i-1] + 1;
            }
            else{
                pref_b[i] = pref_b[i-1];
            }
            if (s[i-1] == 'a'){
                suf_a[i] = suf_a[i-1] - 1;
            }
            else{
                suf_a[i] = suf_a[i-1];
            }
        }
        int cnt = s.size();
        for(int i = 0; i < s.size(); i++){
            cnt = min(cnt, pref_b[i] + suf_a[i] - 1);
        }
        return cnt;
    }
};