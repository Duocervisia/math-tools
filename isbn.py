def calculate_isbn10_check_digit(isbn_partial):
    # Remove any hyphens from the input
    isbn_partial = isbn_partial.replace("-", "")
    
    # Ensure the input is 9 digits long
    if len(isbn_partial) != 9:
        raise ValueError("ISBN partial must be 9 digits long")
    
    # Calculate the check digit
    total = 0
    for i, digit in enumerate(isbn_partial):
        print(f"{i+1}*{digit}", end=" + ")
        total += (i + 1) * int(digit)
    print(f"{10} * c10 = 0 mod 11")
    check_digit = total % 11
    print(f"{total} + 10 * c10 = 0 mod 11")
    if check_digit == 10:
        check_digit = 'X'
    print(f"c10 = {check_digit}")
    
    return str(check_digit)

# Example usage
isbn_partial = "3-528-06580"
check_digit = calculate_isbn10_check_digit(isbn_partial)
isbn_complete = isbn_partial + "-" + check_digit
print("Complete ISBN-10:", isbn_complete)