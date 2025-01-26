def calculate_isbn10_digit(isbn_partial, missing_digit_position):
    # Remove any hyphens from the input
    isbn_partial = isbn_partial.replace("-", "")
    
    # Ensure the input is 9 digits long
    if len(isbn_partial) != 9:
        raise ValueError("ISBN partial must be 9 digits long")
    
    # Calculate the check digit
    total = 0
    missing_digit_passed = False
    for i, digit in enumerate(isbn_partial):
        if i == missing_digit_position - 1:
            print(f"{i+1}xc{i+1}", end=" + ")
            missing_digit_passed = True
        if digit == 'X':
            digit = 10
        if missing_digit_passed:
            print(f"{i+2}x{digit}", end=" + ")
            total += (i + 2) * int(digit)
        else:
            print(f"{i+1}x{digit}", end=" + ")
            total += (i + 1) * int(digit)  

    if missing_digit_position == 10:
        print(f"10xc10", end=" ")


    print(f" = 0 mod 11")
    print(f"{total} + {missing_digit_position} x c{missing_digit_position} = 0 mod 11")
    
    digit = 0
    for i in range(11):
        if (total + missing_digit_position * i) % 11 == 0:
            digit = i
            break
    if digit == 10:
        digit = 'X'

    return str(digit)

# Example usage
isbn_partial = "3-05-501517-"
missing_digit_position = 10
digit = calculate_isbn10_digit(isbn_partial, missing_digit_position)
print("Fehlende Zahl:", digit)