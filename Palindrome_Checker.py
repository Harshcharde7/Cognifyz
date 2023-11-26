def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = ''.join(input_str.split()).lower()
    
    # Check if the string is the same forwards and backwards
    return cleaned_str == cleaned_str[::-1]

# Example usage:
word = input("\n\t\tEnter a word or phrase: ")

if is_palindrome(word):
    print(f"\t\t{word} is a palindrome.\n")
else:
    print(f"\t\t{word} is not a palindrome.\n")
