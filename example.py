# Two sum solution: #############################################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x]+nums[y] == target:
                    return [x,y]
        return []
#######BRUTE FORCE################################################################1

# Valid parentheses solution: #############################################################################
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}','')
            s = s.replace('[]','')
        return s == ''
#######BRUTE FORCE################################################################1
