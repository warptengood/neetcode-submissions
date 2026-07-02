class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            gram = str(sorted(s))
            if gram in groups:
                groups[gram].append(s)
            else:
                groups[gram] = [s]
        
        return list(groups.values())