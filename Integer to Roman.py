def intToRoman(num: int) -> str:
    # Mapping values to symbols in descending order
    # Includes subtractive cases (e.g., 4, 9, 40, etc.)
    val_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    roman_num = ""
    
    for value, symbol in val_map:
        # Determine how many times the current symbol fits
        count, num = divmod(num, value)
        roman_num += symbol * count
        
        # Stop early if num reaches 0
        if num == 0:
            break
            
    return roman_num
