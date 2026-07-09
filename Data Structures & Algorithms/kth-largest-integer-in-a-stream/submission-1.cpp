class KthLargest {
public:
    int k;
    priority_queue<int> q;
    KthLargest(int _k, vector<int>& nums) {
        
        k = _k;
        for (auto it : nums) {
            if (q.size() < k) {
                q.push(-it);
            } else {
                if (-q.top() < it) {
                    q.pop();
                    q.push(-it);
                }
            }
        }
    }
    
    int add(int val) {
        if (q.size() < k) {
            q.push(-val);
        } else {
            if (-q.top() < val) {
                q.pop();
                q.push(-val);
            }
        }
        return -q.top();
    }
};
