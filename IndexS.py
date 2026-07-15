class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Get lengths of both strings
        h_len = len(haystack)
        n_len = len(needle)
        
        # If needle is longer than haystack, it can't be a substring
        if n_len > h_len:
            return -1
            
        # Loop through haystack up to where needle can fit
        for i in range(h_len - n_len + 1):
            # Check if the substring matches the needle
            if haystack[i : i + n_len] == needle:
                return i
                
        # Return -1 if no match is found
        return -1
