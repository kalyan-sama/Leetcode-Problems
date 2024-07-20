'''
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

#Methog-1: using single hashmap

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hashmap = {}
        for i in s:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for i in t:
            if i not in hashmap.keys():
                return False
            hashmap[i] -= 1
            if hashmap[i] == 0:
                del hashmap[i]

        return hashmap == {}

# Time: O(n) {O(S+T)}
# Space: O(n)

#----------------------------------------------------------------------

#Method-2: using 2 hashmaps

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    s_map, t_map = {}, {}
    for i in range(len(s)):
        s_map[s[i]] = 1 + s_map.get(s[i], 0)
        t_map[t[i]] = 1 + t_map.get(t[i], 0)

    for k in s_map:
        if s_map[k] != t_map.get(k, 0):
            return False
    return True

# Time: O(n) {O(S+T)}
# Space: O(n)

#----------------------------------------------------------------------

#Method-3: Sorting

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    return sorted(s) == sorted(t)

# Time: O(nlog(n))
# Space: O(1)
