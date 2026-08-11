class Solution:
    def isPalindrome(self, s):
        s = s.lower()

        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch

        return new == new[::-1]
