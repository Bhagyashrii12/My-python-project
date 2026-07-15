from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        word_counts = Counter(words)
        result = []
        
        # Check all possible offsets within the word length
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            words_used = 0
            
            # Slide the window across the string
            while right + word_len <= s_len:
                # Get the next word from the right
                word = s[right : right + word_len]
                right += word_len
                
                if word in word_counts:
                    current_counts[word] += 1
                    words_used += 1
                    
                    # If we have too many instances of 'word', shift left until valid
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left : left + word_len]
                        current_counts[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    # If all words match exactly, record the starting index
                    if words_used == num_words:
                        result.append(left)
                else:
                    # Invalid word: clear window data and reset left boundary
                    current_counts.clear()
                    words_used = 0
                    left = right
                    
        return result
