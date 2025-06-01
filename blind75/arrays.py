from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        UniqueSet = set()
        for i in nums:
            if i in UniqueSet:
                return True
            UniqueSet.add(i)
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        return all(x == 0 for x in count)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
    def twoSumt(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if j < len(nums):
                    if nums[i] + nums[j] == target:
                        return [i,j]
                j += 1

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return list(anagrams.values())


# Example usage
object = Solution()
print(object.hasDuplicate([1, 2, 3, 4, 5]))  # False
print(object.hasDuplicate([1, 2, 3, 4, 5, 1]))  # True
print(object.isAnagram("anagram", "nagaram"))  # True
print(object.isAnagram("rat", "car"))  # False
print(object.twoSumt([4,5,6], 10))  # [0, 1]
print(object.twoSum([4,5,6], 10))  # [0, 1]  
print(object.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(object.groupAnagrams(["x"]))  # [['x']]        