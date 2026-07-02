class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;
        for (auto val : nums) {
            if (freq.find(val) == freq.end()) {
                freq[val] = 1;
            } else {
                freq[val] += 1;
            }
        }
        vector<pair<int, int>> pr;
        for (auto fr : freq) {
            pr.push_back({-fr.second, fr.first});
        }
        sort(pr.begin(), pr.end());
        vector<int> res;
        int beg = pr[k - 1].first;
        for (int i = 0; i < k; i++) {
            res.push_back(pr[i].second);
        }
        return res;
    }
};
