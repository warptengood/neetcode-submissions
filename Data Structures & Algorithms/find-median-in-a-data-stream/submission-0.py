
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []        

    def topleft(self):
        if len(self.left) == 0:
            return int(2e9)
        return -self.left[0]

    def topright(self):
        if len(self.right) == 0:
            return -int(2e9)
        return self.right[0]
    
    def pushleft(self, val):
        heapq.heappush(self.left, -val)

    def pushright(self, val):
        heapq.heappush(self.right, val)

    def balance(self):
        while abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) < len(self.right):
                val = heapq.heappop(self.right)
                heapq.heappush(self.left, -val)
            else:
                val = -heapq.heappop(self.left)
                heapq.heappush(self.right, val)
    
    def addNum(self, num: int) -> None:
        lefttop = self.topleft()
        if num <= lefttop:
            self.pushleft(num)
        else:
            self.pushright(num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.topleft()
        elif len(self.left) < len(self.right):
            return self.topright()
        else:
            return (self.topleft() + self.topright()) / 2    
        