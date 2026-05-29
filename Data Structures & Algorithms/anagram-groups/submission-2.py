class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs:
            ss = sorted(i)
            ss = "".join(ss)

            if ss not in hashmap:
                hashmap[ss] = []
            
            hashmap[ss].append(i)
        
        return list(hashmap.values())