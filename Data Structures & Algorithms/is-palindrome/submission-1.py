class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str = ''.join(c.lower() for c in s if c.isalnum())
        return formatted_str == formatted_str[::-1]