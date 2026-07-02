class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lst = []
        rst = []
        lb = [None] * len(heights)
        rb = [None] * len(heights) 
        for i, h_i in enumerate(heights):
            j = len(heights) - i - 1
            h_j = heights[j]
            while len(lst) > 0 and lst[-1][0] > h_i:
                lb[lst[-1][1]] = i - 1
                lst.pop()
            lst.append((h_i, i))
            while len(rst) > 0 and rst[-1][0] > h_j:
                rb[rst[-1][1]] = j + 1
                rst.pop()
            rst.append((h_j, j))

        while len(lst) > 0:
            lb[lst[-1][1]] = len(heights) - 1
            lst.pop()
        while len(rst) > 0:
            rb[rst[-1][1]] = 0
            rst.pop()
        print(lb)
        print(rb)
        return max([heights[i] * (lb[i] - rb[i] + 1) for i in range(len(heights))])
        
