class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        edges = {}
        dist = {}
        INF = int(1e9)
        for w in wordList:
            for i in range(len(w)):
                node = w[:i] + '.' + w[i + 1:]
                if node not in edges:
                    edges[node] = []
                edges[node].append(w)

        q = deque()
        q.append(beginWord)
        dist[beginWord] = 0
        while len(q) > 0:
            cur_word = q.popleft()
            for i in range(len(cur_word)):
                node = cur_word[:i] + '.' + cur_word[i + 1:]
                if node not in edges:
                    continue
                for to in edges[node]:
                    if to not in dist or dist[to] > dist[cur_word] + 1:
                        dist[to] = dist[cur_word] + 1
                        q.append(to)
        
        if endWord not in dist:
            return 0
        return dist[endWord] + 1