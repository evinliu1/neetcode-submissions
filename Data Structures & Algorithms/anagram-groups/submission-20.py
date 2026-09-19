class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        res = defaultdict(list)
        for word in strs:
            char_hash = [0] * 26
            for ch in word:
                char_hash[ord(ch) - ord('a')] += 1
            res[tuple(char_hash)].append(word)
        
        return list(res.values())