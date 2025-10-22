class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10                   # Get last digit
            reversed_num = reversed_num * 10 + digit
            x = x // 10                      # Remove last digit
        
        return original == reversed_num
