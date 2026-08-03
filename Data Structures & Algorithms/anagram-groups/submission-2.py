class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a .... z
            for c in s:
                count[ord(c) - ord('a')] += 1
                # ex: [0, 0, 1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 8, ....] 

            res[tuple(count)].append(s)
            """
            res = {
                [ 0, 0 , 1, 0 .... 0] : ["cho", "hoc", "och"],
                [ 1 , 1 , 1, 0, ...0] : ["abc", "bac" , "cab"],
                ..
            }

            """
        
        return list(res.values())
        """
        returns
        [["cho", "hoc", "och"], ["abc", "bac", "cab"]]
        """


                

        