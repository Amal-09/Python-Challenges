def int_to_roman(num):
    roman_numerals = [
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]
    
    result = ""
    for roman, value in roman_numerals:
        while num >= value:
            result += roman
            num -= value
    return result

# Print the first 100 Roman numerals
for i in range(1, 101):
    print(f"{i}: {int_to_roman(i)}")
