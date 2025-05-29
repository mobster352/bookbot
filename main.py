# stats = name of file you want to import from
# get_number_words = name of function in that file
from stats import get_number_words, get_number_characters, sort_character_dictionary
import sys

# get_book_text
# Inputs: -string --path to a file
# Output: -string --contents of a file as a string
def get_book_text(filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    input_book = sys.argv[1]
    text = get_book_text(input_book)
    num_words = get_number_words(text)
    chars = get_number_characters(text)
    sorted_chars = sort_character_dictionary(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")

    print("============= END ===============")

main()