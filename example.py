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

# Valid parentheses solution: #############################################################################
class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []

        # Dictionary to map closing brackets to their corresponding opening brackets
        closetoopen = {")": "(", "]": "[", "}": "{"}

        # Iterate through each character in the input string
        for char in s:
            # If the character is a closing bracket
            if char in closetoopen:
                # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == closetoopen[char]:
                    # If it matches, pop the opening bracket from the stack (valid pair)
                    stack.pop()
                else:
                    # If it doesn't match or the stack is empty, the string is invalid
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # After processing all characters, the stack should be empty if all brackets are matched
        return True if not stack else False
#######O(n) solution################################################################1
