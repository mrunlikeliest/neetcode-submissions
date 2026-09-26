class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(c for c in s if c.isalnum())
        print(t)
        print(t[::-1])
        return t.lower() == t[::-1].lower()
        