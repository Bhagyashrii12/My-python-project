def length_of_longest_substring(s: str) -> int:
    # Maps each character to its last seen index
    char_map = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If the character is in the window, move the left pointer
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
            
        # Update or add the character's latest index
        char_map[char] = right
        
        # Calculate the current window size and update max_length
        max_length = max(max_length, right - left + 1)
        
    return max_length
