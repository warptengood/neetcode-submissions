class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        last = [-n-1] * 26
        for t in tasks:
            cnt[ord(t) - 65] += 1
        
        cycle = 0
        while True:
            is_finished = True
            min_req_cycles = int(2e9)
            task = -1

            for i in range(26):
                if cnt[i] > 0:
                    is_finished = False
                    if cycle - last[i] - 1 >= n:
                        task = i if cnt[i] > cnt[task] or task == -1 else task
                    else:
                        min_req_cycles = min(min_req_cycles, n - cycle + last[i] + 1)

            if is_finished:
                break

            if task == -1:
                cycle += min_req_cycles
            else:
                last[task] = cycle
                cnt[task] -= 1
                cycle += 1
            
        return cycle