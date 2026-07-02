class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (auto s : strs) {   
            res += s;
            res += '|';
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        string cur = "";
        for (auto i : s) {
            if (i == '|') {
                res.push_back(cur);
                cur = "";
            } else {
                cur += i;
            }
        }
        return res;
    }
};
