class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            word_map = [0] * 26
            for ch in word:
                word_map[ord('a') - ord(ch)] += 1
            res[tuple(word_map)].append(word)
        
        return list(res.values())