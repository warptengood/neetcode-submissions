class LRUCache {
private:
    int sz;
    int cur_sz = 0;
    deque<pair<int, int>> d;

public:

    LRUCache(int capacity) {
        sz = capacity;
    }
    
    int get(int key) {
        vector<pair<int, int>> temp;
        pair<int, int> res = {-1, -1};
        while (not d.empty()) {
            pair<int, int> cur = d.back();
            d.pop_back();
            if (cur.first == key) {
                res = cur;
                break;
            }
            temp.push_back(cur);
        }

        for (int i = (int)temp.size() - 1; i >= 0; i--) {
            d.push_back(temp[i]);
        }
        if (res != make_pair(-1, -1)) {
            d.push_back(res);
        }
        return res.second; 
    }
    
    void put(int key, int value) {
        vector<pair<int, int>> temp;
        bool found = false;
        while (not d.empty()) {
            pair<int, int> cur = d.back();
            d.pop_back();
            if (cur.first == key) {
                found = true;
                break;
            }
            temp.push_back(cur);
        }
        for (int i = (int)temp.size() - 1; i >= 0; i--) {
            d.push_back(temp[i]);
        }
        d.push_back({key, value});
        if (!found) {
            cur_sz ++;
            if (cur_sz > sz) {
                d.pop_front();
                cur_sz --;
            }
        }
    }
};
