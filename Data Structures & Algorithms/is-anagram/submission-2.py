class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar
        # racecra

        # will both strings always be the same length? if not I can exit early by comparing lengths
        # can they both be empty strings? if so I can exit early by comparing lengths

        # brute force approach, I can count how many of each letter in each string and save them to two dicts

        s_dict = {}
        t_dict = {}

        for ch in s:
            s_dict[ch] = s_dict.get(ch, 0) + 1
        
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1
        
        return s_dict == t_dict