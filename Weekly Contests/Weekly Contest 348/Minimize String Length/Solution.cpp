class Solution {
public:
    int minimizedStringLength(string s) {
        bool letters[26] = {false};
        for(int i = 0;i < s.length();i++) {
            letters[s[i] - 'a'] = true;
        }
        int count = 0;
        for(int i = 0;i < 26;i++) {
            if(letters[i]) {
                count++;
            }
        }
        return count;
    }
};
