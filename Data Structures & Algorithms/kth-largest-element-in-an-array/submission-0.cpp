class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> q;
        for (auto it : nums) {
            if (q.size() < k) {
                q.push(-it);
            } else if (-q.top() < it) {
                q.pop();
                q.push(-it);
            }
        }
        return -q.top();
    }
};
