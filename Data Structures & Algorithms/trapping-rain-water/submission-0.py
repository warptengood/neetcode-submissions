class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        
        for i in range(1, len(height)):
            left_max[i] = max(height[i - 1], left_max[i - 1])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i + 1], right_max[i + 1])
        
        ans = 0
        for i in range(len(height)):
            ans += max(0, min(left_max[i], right_max[i]) - height[i])
        return ans