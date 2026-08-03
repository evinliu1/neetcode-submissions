class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        word_dict = defaultdict(list)

        for s in strs:
            s_hash = [0] * 26
            for c in s:
                s_hash[ord(c) - ord('a')] += 1
        
            word_dict[tuple(s_hash)].append(s)
        
        for val in word_dict.values():
            result.append(val)
        
        return result