from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = defaultdict(int)

        for let in s:
            map_s[let] += 1
        
        for let in t:
            if let not in map_s:
                return False
            map_s[let] -=1
        
        for key in map_s:
            if map_s[key] != 0:
                return False

        return True
        