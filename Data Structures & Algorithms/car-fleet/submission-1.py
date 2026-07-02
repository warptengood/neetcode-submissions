class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(pos, sp) for pos, sp in zip(position, speed)]
        pos_speed.sort()
        time = [(target - pos) / sp for pos, sp in pos_speed]
        cnt = 1
        st = []
        for t in time:
            while len(st) > 0 and st[-1] <= t:
                st.pop()
            st.append(t)
        return len(st)
"""
p: 9, 6
t: 3, 3
"""