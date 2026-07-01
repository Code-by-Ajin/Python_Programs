def int_to_roman(number: int) -> str:
    """
    Converts an integer to its corresponding Roman numeral string.
    
    Args:
        number (int): An integer between 1 and 3999.
        
    Returns:
        str: The Roman numeral representation of the input integer.
        
    Raises:
        ValueError: If the number is outside the valid Roman numeral range.
    """
    if not (1 <= number <= 3999):
        raise ValueError("Roman numerals handle numbers strictly between 1 and 3999.")

    # Concept 1: Dictionary mapping integer values to Roman symbols (Ordered descending)
    roman_mapping = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C",   90: "XC",  50: "L",  40: "XL",
        10: "X",     9: "IX",   5: "V",   4: "IV",
        1: "I"
    }
    
    roman_numeral = ""
    
    # Concept 2: Loops - Iterating through the dictionary
    for value, symbol in roman_mapping.items():
        # Determine how many times the current symbol fits into the number
        while number >= value:
            roman_numeral += symbol
            number -= value
            
    return roman_numeral


# Concept 3: Function acting as the application controller/entry point
def main():
    print("=========================================")
    print("       ROMAN NUMERAL CONVERTER           ")
    print("=========================================")
    
    try:
        # Prompt user input
        user_input = input("Enter an integer to convert (1-3999): ").strip()
        
        # Validation for non-numeric inputs
        if not user_input.isdigit():
            print("❌ Error: Please enter a valid positive whole number.")
            return

        num = int(user_input)
        
        # Execute conversion
        result = int_to_roman(num)
        
        # Display output
        print("\n--- Output ---")
        print(f"Input : {num}")
        print(f"Roman : {result}")
        print("--------------")

    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
