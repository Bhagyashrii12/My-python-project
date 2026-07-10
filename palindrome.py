def longest_palindrome(s: str) -> str:
    longest = ""
    for i in range(len(s))
        p1 = expand(s, i, i)
        p2 = expand(s, i, i + 1)
        longest = max(longest, p1, p2, key=len)
return longest
def expand(s: str, left: int, right: int) -> str:
    # Walk outwards as long as the letters match
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Return the valid palindrome portion found
    return s[left + 1:right]
