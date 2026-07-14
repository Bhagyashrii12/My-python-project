def generateParenthesis(n):
    res = []
    
    def backtrack(current_s, open_count, close_count):
        # Base case: string is complete
        if len(current_s) == 2 * n:
            res.append(current_s)
            return
        
        # Add open parenthesis if we have more available
        if open_count < n:
            backtrack(current_s + "(", open_count + 1, close_count)
            
        # Add close parenthesis if it won't break the "well-formed" rule
        if close_count < open_count:
            backtrack(current_s + ")", open_count, close_count + 1)
            
    backtrack("", 0, 0)
    return res
