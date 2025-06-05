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

# merge two sorted lists solution: #############################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:# not empty yet, but there are not enough values to analyze
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
#######O(n) solution################################################################1

##Best time to buy stock and sell stock#################################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices array in prices[i]

        
        lowest = prices[0]
        curr_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            elif (price - lowest) > curr_profit:
                curr_profit = price - lowest
        return curr_profit
################################################################################################################################
#

## valid palindrome solution#####
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr = newstr + c.lower()
        return newstr == newstr[::-1]
################################################################################################################################
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1

        while l<r:
            while l< r and not self.alphaNum(s[l]):
                l += 1
            while r> l and not self.alphaNum(s[l]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True
    def alphaNum(self, c):
        (ord('A')<= ord(c) <= ord('Z') or 
         ord('a')<= ord(c) <= ord('z') or 
         ord('0')<= ord(c) <= ord('9')
         )
################################################################################################################################
#########################invert binary tree##################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use recursion
        if not root:return None

        # swap process
        dummy = root.left
        root.left = root.right
        root.right = dummy

        #recursive step
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
##second solution
if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

####################################################################################################