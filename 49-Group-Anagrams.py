from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []


        for s in strs :
            sorted_s = sorted(s)
            anagram_map[tuple(sorted_s)].append(s)
            
        l = []
        for i in anagram_map :
            l.append(anagram_map[i])
        return l
        
        