class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> q;
        for (auto it : stones) {
            q.push(it);
        }
        while (q.size() > 1) {
            int x = q.top();
            q.pop();
            int y = q.top();
            q.pop();
            if (x != y) {
                q.push(max(x,y) - min(x, y));
            }
        }
        if (q.size() == 1) {
            return q.top();
        }
        return 0;
    }
};
