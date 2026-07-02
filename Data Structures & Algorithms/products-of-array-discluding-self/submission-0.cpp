class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pref, suff, res;
        for (int i = 0; i < nums.size(); i++) {
            pref.push_back(i == 0 ? nums[i] : nums[i] * pref.back());
            suff.push_back(nums.size() - i - 1 == nums.size() - 1 ? nums[nums.size() - i - 1] : nums[nums.size() - i - 1] * suff.back());
        }
        reverse(suff.begin(), suff.end());
        for (int i = 0; i < nums.size(); i++) {
            int pred = i == 0 ? 1 : pref[i - 1];
            int post = i == nums.size() - 1 ? 1 : suff[i + 1];
            res.push_back(pred * post);
        }
        return res;
    }
};
