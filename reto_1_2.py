print("----Palindrome Checker----")

def is_palindrome(word: str) -> bool:
    # We first convert the original word to lowercase to avoid issues
    # Later, weconvert the original string into a list of characters
    # Then, we reverse the list using the reverse() method

    lower_word: str = word.lower()
    char_list_original = list(lower_word)
    char_list_reversed = char_list_original.copy()
    char_list_reversed.reverse()

    # Finally, we compare the original list with the reversed one
    return char_list_original == char_list_reversed


original_word: str = input("Enter a word: ")

if is_palindrome(original_word):
    print(f"'{original_word}' is a palindrome.")
else:
    print(f"'{original_word}' is not a palindrome.")    