class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        # Sort the dictionary keys based on their values (frequencies) in descending order
        sorted_keys = sorted(hashmap, key=hashmap.get, reverse=True)
        
        # Take the first k elements from the sorted list
        result = sorted_keys[:k]
        
        return result